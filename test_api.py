import requests
import json
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

def test_get_all_items():
    response = requests.get(f"{BASE_URL}/inventory/items")
    print("\nGET all items:")
    print(response.json())

def test_get_item(item_id):
    response = requests.get(f"{BASE_URL}/inventory/items/{item_id}")
    print(f"\nGET item {item_id}:")
    print(response.json())

def test_create_item():
    new_item = {
        "id": "P010",
        "name": "Test Item",
        "price": 99.99,
        "mfd": datetime.now().strftime("%Y-%m-%d"),
        "ship_date": datetime.now().strftime("%Y-%m-%d"),
        "quantity": 10
    }
    response = requests.post(
        f"{BASE_URL}/inventory/items",
        json=new_item
    )
    print("\nCREATE new item:")
    print(response.json())
    return response.json().get("id")

def test_update_item(item_id):
    updated_item = {
        "name": "Updated Item",
        "price": 149.99,
        "mfd": datetime.now().strftime("%Y-%m-%d"),
        "ship_date": datetime.now().strftime("%Y-%m-%d"),
        "quantity": 20
    }
    response = requests.put(
        f"{BASE_URL}/inventory/items/{item_id}",
        json=updated_item
    )
    print(f"\nUPDATE item {item_id}:")
    print(response.json())

def test_delete_item(item_id):
    response = requests.delete(f"{BASE_URL}/inventory/items/{item_id}")
    print(f"\nDELETE item {item_id}:")
    print(response.json())

if __name__ == "__main__":
    # Test all endpoints
    #test_get_all_items()
    
    # Test getting specific item
    #test_get_item(item_id="P006")
    
    # Create a new item
    new_id = test_create_item()
    
    # Get the created item
    #test_get_item(new_id)
    
    # Update the item
    #test_update_item(new_id)
    
    # Get the updated item
    #test_get_item(new_id)
    
    # Delete the item
    #test_delete_item(new_id)
    
    # Verify deletion
    #test_get_item(new_id)