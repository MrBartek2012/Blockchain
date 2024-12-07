import hashlib
import time
import requests
import json

# Function to mine a block with custom hashing
def mine_block(previous_block, data):
    print("Mining block...")

    # Simple mining process that generates a hash based on the block's data
    new_block = {
        'index': previous_block['index'] + 1,
        'previous_hash': previous_block['hash'],
        'timestamp': time.time(),
        'data': data,
        'hash': ''
    }

    # Simple Proof of Work: Find a hash that starts with '0000'
    difficulty = 4
    new_block['hash'] = calculate_hash(new_block)
    while not new_block['hash'].startswith('0' * difficulty):
        new_block['timestamp'] = time.time()
        new_block['hash'] = calculate_hash(new_block)
    
    # Once mined, return the new block
    print(f"Block successfully mined with hash: {new_block['hash']}")
    return new_block

# Helper function to calculate block hash
def calculate_hash(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

# Function to broadcast the mined block to the network (via POST request)
def broadcast_block(mined_block):
    url = 'http://192.168.1.34:5000/add_block'  # Main node IP address (replace with actual)
    response = requests.post(url, json={'data': mined_block['data']})
    if response.status_code == 200:
        print("Block successfully added to the blockchain!")
    else:
        print("Error adding block to the blockchain.")

# Main mining loop
def mine_and_broadcast():
    # Initialize the blockchain with the Genesis block
    genesis_block = {
        'index': 1,
        'previous_hash': '0',
        'timestamp': time.time(),
        'data': 'Genesis Block',
        'hash': 'genesis_hash'
    }

    previous_block = genesis_block
    while True:
        # Simulate mining a block
        mined_block = mine_block(previous_block, "Block mined with custom coinhash")

        # Broadcast the mined block to the network
        broadcast_block(mined_block)

        # Update the previous block reference for the next iteration
        previous_block = mined_block

        # Wait before mining the next block
        time.sleep(5)

# Run the miner
if __name__ == "__main__":
    mine_and_broadcast()
