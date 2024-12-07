from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# Blockchain variable to store the blockchain
blockchain = []

# Genesis block initialization
blockchain.append({
    'index': 1,
    'previous_hash': '0',
    'timestamp': time.time(),
    'data': 'Genesis Block',
    'hash': 'genesis_hash',
})

@app.route('/add_block', methods=['POST'])
def add_block():
    new_block = request.get_json()

    # Append the new block to the blockchain
    blockchain.append(new_block)

    # Print the new block in the terminal to notify that it was mined
    print(f"New block mined: {new_block}")
    print("Blockchain updated:")
    for block in blockchain:
        print(f"Index: {block['index']}, Hash: {block['hash']}")

    return jsonify({'message': 'Block successfully mined and added to blockchain!'}), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    return jsonify({'blockchain': blockchain})

@app.route('/get_ip', methods=['GET'])
def get_ip():
    return jsonify({'ip': '192.168.1.34'})  # Main node IP

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
