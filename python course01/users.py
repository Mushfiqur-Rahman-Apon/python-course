from abc import ABC
from orders import Order


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)

        if item is None:
            print("Item not found!")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        already_ordered = self.cart.items.get(item, 0)
        available_quantity = item.quantity - already_ordered

        if quantity > available_quantity:
            print("Item quantity exceeded!")
            return

        self.cart.add_item(item, quantity)
        print(f"{item.name} added to cart successfully!")

    def view_cart(self):
        print("\n***** View Cart *****")
        print(f"{'Name':<15}{'Price':<12}{'Quantity':<10}{'Subtotal':<12}")

        if not self.cart.items:
            print("Your cart is empty!")
            return

        for item, quantity in self.cart.items.items():
            subtotal = item.price * quantity

            print(
                f"{item.name:<15}"
                f"{item.price:<12.2f}"
                f"{quantity:<10}"
                f"{subtotal:<12.2f}"
            )

        print(f"\nTotal Price: {self.cart.total_price:.2f}")

    def pay_bill(self):
        if not self.cart.items:
            print("Your cart is empty!")
            return

        for item, quantity in self.cart.items.items():
            if quantity > item.quantity:
                print(f"Insufficient stock for {item.name}!")
                return

        total = self.cart.total_price

        for item, quantity in self.cart.items.items():
            item.quantity -= quantity

        print(f"Total {total:.2f} paid successfully!")
        self.cart.clear()


class Employee(User):
    def __init__(
        self, name, email, phone, address,
        age, designation, salary
    ):
        super().__init__(name, phone, email, address)
        self.age = int(age)
        self.designation = designation
        self.salary = float(salary)


class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()