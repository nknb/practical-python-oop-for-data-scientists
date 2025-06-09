from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import Error
from datetime import datetime

app = Flask(__name__)

# Database connection configuration
DB_CONFIG = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "Nknb1992",
    "port": "5433"
}

def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

# GET all items
@app.route("/inventory/items", methods=['GET'])
def get_all_items():
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500
        
        cur = conn.cursor()
        cur.execute("SELECT * FROM inventory")
        result = cur.fetchall()
        
        # Convert to list of dictionaries
        items = []
        for row in result:
            items.append({
                "id": row[0],
                "name": row[1],
                "price": float(row[2]) if row[2] else None,
                "mfd": row[3].strftime("%Y-%m-%d") if row[3] else None,
                "ship_date": row[4].strftime("%Y-%m-%d") if row[4] else None,
                "quantity": row[5]
            })
        
        cur.close()
        conn.close()
        
        return jsonify({"items": items})
    except Error as e:
        return jsonify({"error": str(e)}), 500

# GET single item by ID
@app.route("/inventory/items/<string:item_id>", methods=['GET'])
def get_item(item_id):
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500
        
        cur = conn.cursor()
        cur.execute("SELECT * FROM inventory WHERE id = %s", (item_id,))
        result = cur.fetchone()
        
        cur.close()
        conn.close()
        
        if result:
            return jsonify({
                "id": result[0],
                "name": result[1],
                "price": float(result[2]) if result[2] else None,
                "mfd": result[3].strftime("%Y-%m-%d") if result[3] else None,
                "ship_date": result[4].strftime("%Y-%m-%d") if result[4] else None,
                "quantity": result[5]
            })
        return jsonify({"error": "Item not found"}), 404
    except Error as e:
        return jsonify({"error": str(e)}), 500

# POST new item
@app.route("/inventory/items", methods=['POST'])
def create_item():
    try:
        data = request.get_json()
        required_fields = ['id', 'name', 'price', 'mfd', 'ship_date', 'quantity']
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500
        
        cur = conn.cursor()
        
        # Check if ID already exists
        cur.execute("SELECT id FROM inventory WHERE id = %s", (data['id'],))
        if cur.fetchone():
            cur.close()
            conn.close()
            return jsonify({
                "error": f"An item with ID '{data['id']}' already exists in the database"
            }), 409  # 409 Conflict
        
        # If ID doesn't exist, create new item
        cur.execute(
            """
            INSERT INTO inventory (id, name, price, mfd, ship_date, quantity) 
            VALUES (%s, %s, %s, %s, %s, %s) 
            RETURNING id
            """,
            (
                data['id'],
                data['name'],
                data['price'],
                data['mfd'],
                data['ship_date'],
                data['quantity']
            )
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        
        cur.close()
        conn.close()
        
        return jsonify({
            "message": "Item created successfully",
            "id": new_id
        }), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500

# PUT update item
@app.route("/inventory/items/<string:item_id>", methods=['PUT'])
def update_item(item_id):
    try:
        data = request.get_json()
        required_fields = ['name', 'price', 'mfd', 'ship_date', 'quantity']
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500
        
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE inventory 
            SET name = %s, price = %s, mfd = %s, ship_date = %s, quantity = %s 
            WHERE id = %s 
            RETURNING id
            """,
            (
                data['name'],
                data['price'],
                data['mfd'],
                data['ship_date'],
                data['quantity'],
                item_id
            )
        )
        result = cur.fetchone()
        conn.commit()
        
        cur.close()
        conn.close()
        
        if result:
            return jsonify({"message": "Item updated successfully"})
        return jsonify({"error": "Item not found"}), 404
    except Error as e:
        return jsonify({"error": str(e)}), 500

# DELETE item
@app.route("/inventory/items/<string:item_id>", methods=['DELETE'])
def delete_item(item_id):
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500
        
        cur = conn.cursor()
        cur.execute("DELETE FROM inventory WHERE id = %s RETURNING id", (item_id,))
        result = cur.fetchone()
        conn.commit()
        
        cur.close()
        conn.close()
        
        if result:
            return jsonify({"message": "Item deleted successfully"})
        return jsonify({"error": "Item not found"}), 404
    except Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)