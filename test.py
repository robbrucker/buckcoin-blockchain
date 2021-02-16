from services.BlockClass import Block
from bson.json_util import dumps, loads
from pprint import pprint

the_chain = Block()

t1 = the_chain.new_transaction('buck', 'e', '300 buckcoins')
t2 = the_chain.new_transaction('e', 'buck', '500 buckcoins')
print("See t3 ", pprint(t2))
t3 = the_chain.new_transaction('e', 'bo jiden', '200 buckcoins')
the_chain.new_block(12345)

t4 = the_chain.new_transaction('buck', 'dog', '300 buckcoins')
t5 = the_chain.new_transaction('dog', 'bo jiden', '500 buckcoins')
t6 = the_chain.new_transaction('bo jiden', 'buck', '200 buckcoins')
the_chain.new_block(234234234)

print("Blockchain: ", the_chain.chain)