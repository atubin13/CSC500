Steve # This program finishes the Online Shopping Cart system started in earlier
# modules. It uses two classes (ItemToPurchase and ShoppingCart) and a
# menu-driven loop (print_menu) that runs until the user chooses "q".


class ItemToPurchase:
    """One product the customer wants to buy."""

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
    """A customer's cart: their name, the date, and a list of items."""

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
        print(f"'{item_to_purchase.name}' was added to the cart.")

    def remove_item(self, item_name):
        # Search the list by name (upper/lower case is ignored).
        for item in self.cart_items:
            if item.name.lower() == item_name.lower():
                self.cart_items.remove(item)
                print(f"'{item.name}' was removed from the cart.")
                return

        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        # item_to_purchase is a temporary object that carries the item's
        # name plus the new values. Only values that were changed from the
        # defaults ("none" or 0) are applied.
        for item in self.cart_items:
            if item.name.lower() == item_to_purchase.name.lower():
                if item_to_purchase.description != "none":
                    item.description = item_to_purchase.description

                if item_to_purchase.price != 0:
                    item.price = item_to_purchase.price

                if item_to_purchase.quantity != 0:
                    item.quantity = item_to_purchase.quantity

                print(f"'{item.name}' was updated.")
                return

        print("Item not found in cart. Nothing modified.")

    def get_num_items(self):
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
        print(f"Number of Items: {self.get_num_items()}")
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


def get_text(prompt):
    """Ask until the user types something that is not blank."""
    while True:
        text = input(prompt).strip()

        if text == "":
            print("Invalid entry. This cannot be blank.")
        else:
            return text


def get_price(prompt):
    """Ask until the user types a valid price of zero or more."""
    while True:
        try:
            price = float(input(prompt).replace("$", ""))

            if price < 0:
                print("Invalid price. Price cannot be negative.")
            else:
                return price
        except ValueError:
            print("Invalid price. Please enter a number, such as 2.99.")


def get_quantity(prompt):
    """Ask until the user types a whole number greater than 0."""
    while True:
        try:
            quantity = int(input(prompt))

            if quantity <= 0:
                print("Invalid quantity. Quantity must be greater than 0.")
            else:
                return quantity
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")


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

        if user_choice == "a":
            print("ADD ITEM TO CART")
            item_name = get_text("Enter the item name: ")
            item_description = get_text("Enter the item description: ")
            item_price = get_price("Enter the item price: ")
            item_quantity = get_quantity("Enter the item quantity: ")

            new_item = ItemToPurchase(
                item_name,
                item_price,
                item_quantity,
                item_description
            )

            shopping_cart.add_item(new_item)

        elif user_choice == "r":
            print("REMOVE ITEM FROM CART")
            item_name = get_text("Enter name of item to remove: ")
            shopping_cart.remove_item(item_name)

        elif user_choice == "c":
            print("CHANGE ITEM QUANTITY")
            item_name = get_text("Enter the item name: ")
            item_quantity = get_quantity("Enter the new quantity: ")

            # Temporary object that only carries the name and new quantity.
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

        elif user_choice == "q":
            print("Thank you for shopping. Goodbye!")

        else:
            print("Invalid option. Please enter a, r, c, i, o, or q.")


if __name__ == "__main__":
    customer_name = input("Enter customer's name: ").strip()
    current_date = input("Enter today's date: ").strip()

    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)