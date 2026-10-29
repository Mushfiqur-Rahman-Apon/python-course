from food_item import FoodItem

from menu import Menu
from users import Customer, Admin, Employee
from restaurent import Restaurent
from orders import Order

mamar_restaurent = Restaurent("Mamar Restaurement")
def customer_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    addrsess = input("Enter Your Address : ")
    Customer = Customer(name=name, email=email, phone=phone,
    address=addrsess)
 
    while True:
        print(f"welcome {Customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. Add item to cart")
        print("4. PayBill")
        print("5. Exit")
        
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            Customer.view_menu(mamar_restaurent)
        elif choice == 2:
            item_name = input("Enter item name : ")  
            item_quantity = int(input("Enter item quantity : ")) 
            Customer.add_to_cart(mamar_restaurent, item_name, item_quantity)
        elif choice == 3:
            Customer.view_cart()
        elif choice == 4:   
            Customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input")          
        


def admin_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    addrsess = input("Enter Your Address : ")
    admin = Customer(name=name, email=email, phone=phone,
    address=addrsess)
 
    while True:
        print(f"welcome {admin.name}!!")
        print("1. View New Item")
        print("2. Add item to Employee")
        print("3. view Emplyee")
        print("4. pay Items")
        print("5.Delete Item")
        print("6. Exit")
        
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            item_name = input("Enter Item Name : ")
            item_price = int(input("Enter Item price : "))
            item_quantity = int(input("Enter Item Quantity : "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_restaurent, item)
            
           
        elif choice == 2:
            name = input("Enter employee name : ")
            phone = input("Enter employee phone : ")
            email = input("Enter employee email : ")
            designation = input("Enter employee designation : ")
            age = input("Enter employee age :")
            salary = input("Enter employee salary : ")
            address = input("Enter employee address : ")
            admin.add_employee(name,email, phone, address, age, designation, salary)
            
            
        elif choice == 3:
            admin.view_employee(mamar_restaurent)
        elif choice == 4:   
            admin.view_menu(mamar_restaurent)
        elif choice == 5:
            admin.remove_item(mamar_restaurent, item_name)
        elif choice == 6:
            break    
        else:
            print("Invalid Input")          
        
                
while True:
    print("Welcome")        
    print("1. customer")        
    print("2. Admin")        
    print("3. Exit")        
    choice = int(input("Enter your choice : "))
    if choice == 1:  
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break            
    else:
        print("Invalid Input!!")
