from services.BlockClass import Block
from pprint import pprint
import names
from random import randrange


all_chains = []
for _ in range(20):
    the_chain = Block()
    for __ in range(20):
        t = the_chain.new_transaction(names.get_last_name() + ' ' + names.get_last_name(), names.get_last_name() + ' ' + names.get_last_name(), randrange(10000))
    the_chain.new_block(randrange(1000000))
    all_chains.append(the_chain.chain)

print("Blockchain: ", all_chains)