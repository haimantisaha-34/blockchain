blockchain=[]

def get_value_blockchain():
    return blockchain [-1]

def add_value(transaction_amount,last_transaction=[1]):
    blockchain.append([last_transaction,transaction_amount])
    

add_value(2)
add_value(34,get_value_blockchain())
add_value(86,get_value_blockchain())

print(blockchain)
