from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize an in-memory list to store items
items = []

# Create an item (Create operation)
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if 'name' in data and 'price' in data:
        item = {
            'name': data['name'],
            'price': data['price']
        }
        items.append(item)
        return jsonify({'message': 'Item created successfully', 'item': item}), 201
    return jsonify({'message': 'Invalid request data'}), 400

# Retrieve all items (Read operation)
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})

# Retrieve a specific item by name (Read operation)
@app.route('/items/<string:item_name>', methods=['GET'])
def get_item(item_name):
    for item in items:
        if item['name'] == item_name:
            return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

# Update an item by name (Update operation)
@app.route('/items/<string:item_name>', methods=['PUT'])
def update_item(item_name):
    data = request.get_json()
    for item in items:
        if item['name'] == item_name:
            if 'price' in data:
                item['price'] = data['price']
                return jsonify({'message': 'Item updated successfully', 'item': item})
    return jsonify({'message': 'Item not found'}), 404

# Delete an item by name (Delete operation)
@app.route('/items/<string:item_name>', methods=['DELETE'])
def delete_item(item_name):
    for item in items:
        if item['name'] == item_name:
            items.remove(item)
            return jsonify({'message': 'Item deleted successfully'})
    return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
