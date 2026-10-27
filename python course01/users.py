
from abc import ABC





class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        
class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
        
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        print(item.quantity)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            else:
                item.quantity = quantity
                self.cart = Order()
                print("item added")
        else:
            print("Item not found")
    def view_cart(self):
        print("**view Cart**")
        print("Name\tprice\tQuantity")   
        for item, quantity in self.cart.items.items():  
            print(f"{item.name} {item.price} {item.quantity}") 
            print(f"Total Price : {self.cart.total_price}")
         
         
         
class Order:
    def __init__(self) -> None:
        self.items = {}
     
    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity    
        else:
            self.items[item] = item.quantity
    def remove(self, item):
        if item in self.items:
            del self.items[item]       
         
    @property  
    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())
    
    def clear(self):
        self.items = {}       
class Employee(User):
    def __init__(self, name, email, phone, address,age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
             
                  

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)
        
    def add_empolyee(self,restaurnt, employee):
            restaurnt.add_employee(employee)
        
    def view_emplyee(self, restaurent):
            restaurent.view_employee()
        
    def add_new_item(self,restaurent, item): 
        restaurent.menu.add_menu_item(item)   
        
    def remove_item(self,restaurent, item): 
        restaurent.menu.remove_item(item) 
class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees =[] #cta hoche amader data
        self.menu = Menu()
         
    def add_employee(self, employee):  
        self.employees.append(employee)
        
    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)
        
        
        
class Menu:
    def __init__(self):
        self.items = [] #items er daa base
    
    def add_menu_item(self, item):
        self.items.append(item)    
    
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return self.item
            return None
        def remove_item(self, item_name):
            item = self.find_item(item_name)
            if item:
                self.items.remove(item)
                print("Item deleted") 
            else:
                print("item not found")
                
          
    
    def show_menu(self):
        print("*****Menu*****")  
        print("Name\tPrice\tQuanity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")        
            
            
class FoodItem:
    def __init__(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
            

mamar_res = Restaurent("Mamar Restaurent")       
mn = Menu()
item = FoodItem("Pizza", 12.45, 10)
item2 = FoodItem("Burger", 10, 30)

admin = Admin("Rahim", "Rahim@gmail.com",123123, "Dhaka")
mn.add_menu_item(item)
mn.add_menu_item(item2)

customer1 = Customer("Rahim", "Rahim@gmail.com",123123, "Dhaka")
customer1.view_menu(mamar_res)

item_name = input("Enter item Name:")
item_quantity = int(input("Enter Item Quantity"))

customer1.add_to_cart(mamar_res, item_name, item_quantity)
customer1.view_cart()