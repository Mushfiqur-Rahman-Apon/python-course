class Animal:
    def eat(self):
        print('hey nanal!, eating banana')
    def move(self):
        pass
   
class Monkey(Animal):    
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        
        self.name = 'Monkey'
        self.name = name
        super().__init__()
        
layka = Monkey('lucky')
layka.eat()        