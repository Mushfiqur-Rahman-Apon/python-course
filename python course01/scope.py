balance = 3000

def buy_things(item, price):

    print(f'previous balance value', balance)

    balance = 500

    balance = balance - price

    print(f'balance after buying {item}', balance)

buy_things('sunglass', 1000)