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


cart_items = []

while True:
    item_name = input("Enter the item name or type quit to stop: ").strip()

    if item_name.lower() == "quit":
        break

    while item_name == "":
        print("Invalid item name. Item name cannot be blank.")
        item_name = input("Enter the item name or type quit to stop: ").strip()

        if item_name.lower() == "quit":
            break

    if item_name.lower() == "quit":
        break

    while True:
        try:
            item_price = float(input("Enter the item price: ").replace("$", ""))

            if item_price < 0:
                print("Invalid price. Price cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid price. Please enter a number, such as 2.99.")

    while True:
        try:
            item_quantity = int(input("Enter the item quantity: "))

            if item_quantity <= 0:
                print("Invalid quantity. Quantity must be greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid quantity. Please enter a whole number, such as 1, 2, or 10.")

    item_description = input("Enter the item description: ").strip()

    while item_description == "":
        print("Invalid description. Description cannot be blank.")
        item_description = input("Enter the item description: ").strip()

    item = ItemToPurchase(
        item_name,
        item_price,
        item_quantity,
        item_description
    )

    cart_items.append(item)

    print("Item added to cart.\n")


print("\nTOTAL LIST")

cart_subtotal = 0

for item in cart_items:
    item.print_item_subtotal()
    cart_subtotal += item.price * item.quantity

cart_total = cart_subtotal * 1.085

print(f"\nSubtotal: ${cart_subtotal:.2f}")
print(f"Total with tax: ${cart_total:.2f}")