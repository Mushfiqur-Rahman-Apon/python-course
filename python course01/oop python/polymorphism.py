#  poly --> many (multiple)
#  morph --> shape

class Animal:
    def __init__(self,name) -> None:
        self.name = name
    
    def make_sound(self):
        print('animal making some sound')
        
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
don = Cat('Real() -> None')
don.make_sound()                    