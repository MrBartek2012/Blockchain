from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

# Endpoint to get the full blockchain
@app.route('/blocks', methods=['GET'])
def get_blocks():
    return jsonify(blockchain.get_chain())

# Endpoint to mine a new block (triggered by a miner)
@app.route('/mine', methods=['POST'])
def mine_block():
    data = request.json.get('data')
    blockchain.add_block(data)
    return jsonify({"message": "Block mined successfully!"})

# Endpoint to add a block from another node
@app.route('/add_block', methods=['POST'])
def add_block():
    block_data = request.json
    blockchain.add_block(block_data['data'])
    return jsonify({"message": "Block added successfully!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
