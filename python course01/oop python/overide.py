class Person:
    def _init_(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.height = weight
    def eat(self):
        print('vat mangso polau korma')
        
    def exercise(self):
        print('gym e posia diya hudai gham jorai')  
        
class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team  
        super().__init__(name, age, height, weight)
        
    def eat(self):
        print('vegetavles')    
        
sakib = Cricketer('sakib', 38, 68.91, 'BD')
sakib.eat()                 
sakib.exercise()

print()