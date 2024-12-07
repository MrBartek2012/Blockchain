from flask import Flask, jsonify, request
import json
import hashlib
import time

app = Flask(__name__)

# Simple Blockchain setup
blockchain = []

# Helper function to calculate block hash
def calculate_hash(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

# Genesis block (first block in the chain)
def create_genesis_block():
    return {
        'index': 1,
        'previous_hash': '0',
        'timestamp': time.time(),
        'data': 'Genesis Block',
        'hash': 'genesis_hash'
    }

# Create initial blockchain with Genesis block
blockchain.append(create_genesis_block())

# Endpoint to get the current blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    return jsonify({'blockchain': blockchain})

# Endpoint to add a new block (mined by other nodes)
@app.route('/add_block', methods=['POST'])
def add_block():
    data = request.get_json()
    new_block = {
        'index': len(blockchain) + 1,
        'previous_hash': blockchain[-1]['hash'],
        'timestamp': time.time(),
        'data': data['data'],
        'hash': calculate_hash(data)
    }
    blockchain.append(new_block)
    return jsonify({'message': 'Block successfully added to blockchain!'})

# Run the Flask app on all network interfaces (0.0.0.0)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
