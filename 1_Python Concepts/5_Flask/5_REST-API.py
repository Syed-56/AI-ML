from flask import Flask, jsonify, request
app = Flask(__name__)
items = [
    {'id': 1, 'name': 'Item1', 'description': 'This is item 1'},
    {'id': 2, 'name': 'Item2', 'description': 'This is item 2'}
]

@app.route('/')
def home():
    return "Welcome to the sample to-do list app"

if __name__ == '__main__':
    app.run(debug=True)
    
#GET
#retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)   #jsonify(): converts a Python dict/list into a proper JSON HTTP response (sets the correct Content-Type: application/json header too).

#retrieve single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)    #next(): returns the first matching element from an iterable/generator, or the given default (None here) if nothing matches — avoids writing a manual loop with a break.
    if item is None:
        return jsonify({'error': 'Item not found'})
    return jsonify(item)

#POST
#create a new item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({'error': 'Item must have a name'})

    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json.get('description', "")
    }
    items.append(new_item)
    return jsonify(new_item)

#PUT 
#update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'})

    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

#DELETE
#remove an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result': 'Item deleted'})