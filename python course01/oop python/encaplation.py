# encapsulation --> hide details
# access nodifier: puvlice, protected, private

class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name
        self.balance = initial_deposit
        
    def deposit(self, amount):
        self.balance += amount
        
    def get_balance(self):
        return self.__balance            
      
rafsun = Bank('Choooto bro', 10000)

print(rafsun.holder_name)
rafsun.balance = 0
print(rafsun.get_balance)
# print(rafsun._branch)

        