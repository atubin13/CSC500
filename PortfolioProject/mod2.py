# Implement input() statements to gather data from the user.
# Assign this input to appropriately named variables.
# Perform at least two basic arithmetic expressions using the gathered data (e.g., calculating a subtotal).
# For your final project, you will complete the Online Shopping Cart system.
# This involves refining your previous milestones and implementing the remaining functionality.

# First class should be ItemToPurchase
# Need to include name, price, quantity, description
# Key method will be print_item_cost()

class ItemToPurchase:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def print_item_subtotal(self):
        subtotal = self.price * self.quantity
        print(f"Subtotal: {self.name} {self.quantity} @ ${self.price} = ${subtotal:.2f}")

    def print_item_cost(self):
        total = (self.price * self.quantity) * 1.085
        print(f"Total with tax: ${total:.2f}")



item_name = input("Enter the item name: ")
item_price = float(input("Enter the item price: ").replace("$", ""))
item_quantity = int(input("Enter the item quantity: "))
item_description = input("Enter the item description: ")

item = ItemToPurchase(
    item_name,
    item_price,
    item_quantity,
    item_description
)

item.print_item_subtotal()
item.print_item_cost()