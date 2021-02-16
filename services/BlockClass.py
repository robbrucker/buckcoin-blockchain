import hashlib
import json
from time import time
import pymongo
from bson.json_util import dumps, loads

class Block:

    def __init__(self):

        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["blockchain_db"]
        self.ledger = db["ledger"]
        self.chain = self.ledger.find()
        print("See the chain ", self.chain)
        self.genesis_key = "How much wood could a wood chuck chuck if a wood chuck could chuck wood"
        self.pending_transactions = []
        self.new_block(previous_hash=self.genesis_key, proof=100, is_genesis=True)

        print(self.chain)



    def new_block(self, proof, previous_hash=None, is_genesis=False):
        block = {
            'id': self.chain.count() + 1,
            'index': self.chain.count() + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain)
        }
        self.pending_transactions = []
        if(is_genesis != True):
            record = self.ledger.insert_one(block)
            print("stored record ", record)
        else:
            old_record = self.ledger.find({"previous_hash": self.genesis_key})
            print("See count ", old_record.count())
            if old_record.count() != 0:
                print("Genesis already exists")
                record = {}
            else:
                record = self.ledger.insert_one(block)
                print("stored record ", record)



        return record



    def new_transaction(self, sender, recipient, amount, type='buckcoin'):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'type': type
        }
        self.pending_transactions.append(transaction)
        return self.last_block

    def hash(self, block):
        string_object = dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash= hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


    @property
    def last_block(self):
        return self.ledger.find().sort([('timestamp', -1)]).limit(1)
