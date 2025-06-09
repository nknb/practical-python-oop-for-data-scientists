from flask import Flask, request, jsonify

app = Flask(__name__)

fruits = []

# GET : voir la liste
@app.route('/fruits', methods=['GET'])
def get_fruits():
    return jsonify(fruits)

# POST : ajouter un fruit
@app.route('/fruits', methods=['POST'])
def ajouter_fruit():
    data = request.get_json()
    fruits.append(data)
    return jsonify({"message": "Fruit ajouté"}), 201

if __name__ == '__main__':
    app.run(debug=True)