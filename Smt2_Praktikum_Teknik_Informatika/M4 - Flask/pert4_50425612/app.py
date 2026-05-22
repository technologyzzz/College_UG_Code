from flask import Flask, jsonify, request
import json
app = Flask(__name__)
datas = [
    {
        'id': 1,
        'items': [
            {   'title': 'Madilog',
                'author': 'Tan Malaka',
                'price': 84000
                }
        ]
    }, {
        'id': 2,
        'items': [
            {
                'title': 'Animal Farm',
                'author': 'George Orwell',
                'price': 50000
            }
        ]
    }
]
def format_rupiah(amount):
    return f"Rp{amount:,.0f}".replace(",", ".")

@app.route('/book')
def getAll():
    formatted_datas = []
    for data in datas:
        formatted_data = {
            'id': data['id'],
            'items': []
        }
        for item in data['items']:
            formatted_item = {
                'title': item['title'],
                'author': item['author'],
                'price': format_rupiah(item['price'])  
            }
            formatted_data['items'].append(formatted_item)
        formatted_datas.append(formatted_data)
    return jsonify(formatted_datas)
@app.route('/book/<int:id>')
def getbyId(id):
    for data in datas:
        if data['id'] == id:
            formatted_data = {
                'id': data['id'],
                'items': []
            }
            for item in data['items']:
                formatted_item = {
                    'title': item['title'],
                    'author': item['author'],
                    'price': format_rupiah(item['price']) # Format harga disini
                }
                formatted_data['items'].append(formatted_item)
            return jsonify(formatted_data)
    return jsonify({'message': 'Data not found'})
@app.route('/book', methods=["POST"])
def addBook():
    req_data = request.get_json()
    
    if not all(key in req_data for key in ['id', 'items']):
        return jsonify({'message': 'Missing required fields (id, items)'}), 400
    
    if not isinstance(req_data['items'], list):
        return jsonify({'message': "'items' should be a list"}), 400
    for item in req_data['items']:
        if not all(k in item for k in ['title', 'author', 'price']):
             return jsonify({'message': 'Each item in \'items\' should contain title, author, and price'}), 400
        if not isinstance(item['price'], (int, float)):
            return jsonify({'message': 'Price must be a number'}), 400
            
    new_data = {
        'id': req_data['id'],
        'items': req_data['items']
    }
    datas.append(new_data)
    return jsonify(new_data), 201  
@app.route('/book/<int:id>', methods=["DELETE"])
def deleteBook(id):
    global datas 
    for index, data in enumerate(datas): 
        if data['id'] == id:
            del datas[index] 
            return jsonify({'message': 'Book deleted successfully'}), 200
    return jsonify({'message': 'Book not found'}), 404

@app.route('/')
def home():
    return "Halo Maulana Abdul Aziz !"

if __name__=='__main__':
    app.run(debug=True)