import time
from blockchain import Blockchain

def mine_new_block():
    blockchain = Blockchain()
    while True:
        blockchain.add_block(f"Block Data {time.time()}")
        time.sleep(5)  # Optional: Add a delay between mining new blocks

if __name__ == "__main__":
    mine_new_block()
