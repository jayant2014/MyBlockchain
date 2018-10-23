#!/usr/bin/python

import hashlib
import datetime

# Defining block data structure
class Block:
    blkNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def get_hash(self):
        '''
        Create the block hash and return it
        '''
        blk_hash = hashlib.sha256()
        blk_hash.update(str(self.nonce).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.blkNo).encode('utf-8'))
        return blk_hash.hexdigest()

    def __str__(self):
        '''
        Prints the value of the block
        '''
        return "Block Hash: " + str(self.get_hash()) + "\nBlock Number: " + str(self.blkNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

# Defining blockchain data structure
class Blockchain:
    
    difficulty = 20
    maxNonce = 2**32
    target_hash = 2 ** (256-difficulty)

    # Initializing genesis block
    block = Block("Genesis")
    head = block

    def add_block(self, block):
        '''
        Adding block
        '''
        block.previous_hash = self.block.get_hash()
        block.blkNo = self.block.blkNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine_block(self, block):
        '''
        Mining block, whether we can add block or not
        '''
        print(self.target_hash) 
        for n in range(self.maxNonce):
            if int(block.get_hash(), 16) <= self.target_hash:
                self.add_block(block)
                print(block)
                break
            else:
                block.nonce += 1

    def mine_nblocks(self, no):
        '''
        Mine n number of blocks
        '''
        for n in range(no):
            blockchain.mine_block(Block("Block " + str(n+1)))

# Initialize blockchain
blockchain = Blockchain()

blockchain.mine_nblocks(5)
