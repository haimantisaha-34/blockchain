blockchain=[[1]]

def get_value_blockchain():
    return blockchain [-1]

def add_value(transaction_amount):
    blockchain.append([get_value_blockchain(),transaction_amount])
    

add_value(2)
add_value(34)
add_value(86)

print(blockchain)
