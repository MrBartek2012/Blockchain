import hashlib
import time
import requests

# Simple custom coinhash (easy hashing algorithm)
def coinhash(data):
    return hashlib.md5(data.encode()).hexdigest()  # Using MD5 for simplicity

# Simulating mining by creating a block with custom hashing
def mine_block(blockchain, data):
    previous_block = blockchain[-1] if blockchain else None
    index = len(blockchain) + 1
    previous_hash = previous_block['hash'] if previous_block else '0'
    
    new_block = {
        'index': index,
        'previous_hash': previous_hash,
        'timestamp': time.time(),
        'data': data,
        'hash': coinhash(data)  # Applying custom hashing
    }
    
    # After mining the block, send it to the server (other computers) to be added to the blockchain
    try:
        print("Mining block...")
        response = requests.post('http://192.168.1.34:5000/add_block', json=new_block)  # Update with your server IP
        if response.status_code == 200:
            print(response.json()['message'])
    except requests.exceptions.RequestException as e:
        print(f"Error broadcasting mined block: {e}")

# Main mining logic
def mine():
    # Get the current blockchain from the network
    try:
        response = requests.get('http://192.168.1.34:5000/get_chain')  # Fetch current blockchain
        blockchain = response.json()['blockchain']
        print(f"Blockchain retrieved: {blockchain}")

        # Mine a block (you can add your own data to mine)
        data = 'Block mined with custom coinhash'
        mine_block(blockchain, data)  # Mine the block and broadcast it
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching blockchain: {e}")

if __name__ == '__main__':
    mine()
