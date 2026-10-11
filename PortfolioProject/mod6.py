class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def print_item_cost(self):
        total = self.price * self.quantity
        print(f"{self.name} {self.quantity} @ ${self.price:.2f} = ${total:.2f}")

    def print_item_description(self):
        print(f"{self.name}: {self.description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                return

        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.name == item_to_purchase.name:
                if item_to_purchase.description != "none":
                    item.description = item_to_purchase.description

                if item_to_purchase.price != 0:
                    item.price = item_to_purchase.price

                if item_to_purchase.quantity != 0:
                    item.quantity = item_to_purchase.quantity

                return

        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0

        for item in self.cart_items:
            total_quantity += item.quantity

        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0

        for item in self.cart_items:
            total_cost += item.price * item.quantity

        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print()
        print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_description()


def print_menu(shopping_cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""

    user_choice = ""

    while user_choice != "q":
        print(menu)

        user_choice = input("Choose an option: ").lower().strip()

        while user_choice not in ["a", "r", "c", "i", "o", "q"]:
            user_choice = input("Choose an option: ").lower().strip()

        if user_choice == "a":
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name: ").strip()
            item_description = input("Enter the item description: ").strip()

            while True:
                try:
                    item_price = float(input("Enter the item price: ").replace("$", ""))

                    if item_price < 0:
                        print("Invalid price. Price cannot be negative.")
                    else:
                        break
                except ValueError:
                    print("Invalid price. Please enter a number.")

            while True:
                try:
                    item_quantity = int(input("Enter the item quantity: "))

                    if item_quantity <= 0:
                        print("Invalid quantity. Quantity must be greater than 0.")
                    else:
                        break
                except ValueError:
                    print("Invalid quantity. Please enter a whole number.")

            new_item = ItemToPurchase(
                item_name,
                item_price,
                item_quantity,
                item_description
            )

            shopping_cart.add_item(new_item)

        elif user_choice == "r":
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove: ").strip()
            shopping_cart.remove_item(item_name)

        elif user_choice == "c":
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ").strip()

            while True:
                try:
                    item_quantity = int(input("Enter the new quantity: "))

                    if item_quantity < 0:
                        print("Invalid quantity. Quantity cannot be negative.")
                    else:
                        break
                except ValueError:
                    print("Invalid quantity. Please enter a whole number.")

            modified_item = ItemToPurchase(
                name=item_name,
                quantity=item_quantity
            )

            shopping_cart.modify_item(modified_item)

        elif user_choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()

        elif user_choice == "o":
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()


if __name__ == "__main__":
    customer_name = input("Enter customer's name: ").strip()
    current_date = input("Enter today's date: ").strip()

    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)