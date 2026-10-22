class User:
    def __init__(self,name, age, money) -> None :
        self._name = name
        self._age = self._age
        self.__money = money
        
    @property
    def age(self):
        return self._age   
    
    def salaary(self):
        return self.__money 
    
    
        
        
samsu = User('Kopa, 21, 12000')
        
print(samsu.__money)
print(samsu.age())
samsu.alary
    