import hashlib
import time
import random

# Custom Hash Function (replace with your own logic)
def custom_hash(data):
    return str(hash(data))

# Block class
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.nonce = nonce

    # Create a custom block hash (to be mined)
    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return custom_hash(block_string)

# Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    # Create the first block (genesis block)
    def create_genesis_block(self):
        genesis_block = Block(0, "0", time.time(), "Genesis Block", "0")
        self.chain.append(genesis_block)

    # Add a new block to the chain (after mining)
    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), last_block.hash, time.time(), data, "0")
        self.mine_block(new_block)  # Mining the new block
        self.chain.append(new_block)

    # Proof of Work (mining)
    def mine_block(self, block, difficulty=4):
        block.nonce = 0
        while True:
            block.hash = block.calculate_hash()
            if block.hash[:difficulty] == '0' * difficulty:
                print(f"Block mined: {block.hash}")
                break
            block.nonce += 1

    # Get the blockchain as a list of dictionaries
    def get_chain(self):
        return [block.__dict__ for block in self.chain]

# Example Usage:
if __name__ == '__main__':
    blockchain = Blockchain()
    blockchain.add_block("Block 1 Data")
    blockchain.add_block("Block 2 Data")

    # Print the blockchain
    for block in blockchain.get_chain():
        print(block)
