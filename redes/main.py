import asyncio
import hashlib
import socket
import multiprocessing as mp
import datetime
from redes import *

class Blockchain:
 
    # This function is created to create the very first block and set its hash to "0"
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    # This function is created to add further blocks into the chain (inclusão)
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
 
    # This function is created to display the previous block
    def print_previous_block(self):
        return self.chain[-1]
 
    # This is the function for proof of work and used to successfully mine the block
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
 
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
 
        return new_proof

    def hash(self, block):
            return hashlib.sha256(block.encode()).hexdigest()
 
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
 
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
 
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
 
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
 
        return True
    
    # Mining a new block
    def mine_block(self):
        previous_block = blockchain.print_previous_block()
        previous_proof = previous_block['proof']
        proof = blockchain.proof_of_work(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(proof, previous_hash)
    
        response = {'message': 'A block is MINED',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'proof': block['proof'],
                    'previous_hash': block['previous_hash']}
    
        return response
    
    # Check validity of blockchain
    def valid():
        valid = blockchain.chain_valid(blockchain.chain)
    
        if valid:
            response = {'message': 'The Blockchain is valid.'}
        else:
            response = {'message': 'The Blockchain is not valid.'}
        return response
    
    # Divulgação e consenso (faltam)

    '''
    def broadcast_block(self, chain):
    #precisa da lista de pares para enviar a 'chain'



    def consenso(self, chain):
    #depende do tamanho da cadeia
    '''

# Create the object of the class blockchain
blockchain = Blockchain()

#https://docs.python.org/pt-br/3/library/socket.html#socket.socket

#async def blockchain_server(port: int):
#    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    sock.bind((socket.gethostname(), port))
#    sock.listen(10)
#    clients = {}

# Display blockchain
def display_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return response

 