"""
Week 7 - OOP Mini Project: Inventory Management System

Rebuilds the idea of a stock/inventory tracker (similar in spirit to the
Shopping Cart and Dictionaries assignments from earlier weeks) using
classes and objects instead of standalone functions and dictionaries.

Concepts practiced:
- Classes and objects (Item, Inventory)
- Instance attributes and methods (self)
- Encapsulating related data and behavior together
- File persistence through instance methods (save_to_file / load_from_file)
"""


class Item:
    """Represents a single inventory item."""

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        """Returns the total value of this item (quantity * price)."""
        return self.quantity * self.price

    def __str__(self):
        return (f"{self.name} | Qty: {self.quantity} | "
                f"Price: {self.price:.2f} | Total: {self.total_value():.2f}")


class Inventory:
    """Manages a collection of Item objects, with persistence to a file."""

    def __init__(self, filename="inventory_data.txt"):
        self.items = []
        self.filename = filename
        self.load_from_file()

    def find_item(self, name):
        """Returns the Item matching the given name, or None."""
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

    def add_item(self, name, quantity, price):
        """Adds a new item, or increases quantity if it already exists."""
        existing = self.find_item(name)
        if existing:
            existing.quantity += quantity
            print(f"Updated quantity for '{name}'. New quantity: {existing.quantity}")
        else:
            self.items.append(Item(name, quantity, price))
            print(f"Added new item '{name}'.")

    def remove_item(self, name):
        """Removes an item from the inventory by name."""
        item = self.find_item(name)
        if item:
            self.items.remove(item)
            print(f"Removed '{name}' from inventory.")
        else:
            print(f"Item '{name}' not found.")

    def update_quantity(self, name, new_quantity):
        """Sets an item's quantity to a specific value."""
        item = self.find_item(name)
        if item:
            item.quantity = new_quantity
            print(f"Updated '{name}' quantity to {new_quantity}.")
        else:
            print(f"Item '{name}' not found.")

    def total_inventory_value(self):
        """Returns the combined value of every item in the inventory."""
        return sum(item.total_value() for item in self.items)

    def display_all(self):
        """Prints every item currently in the inventory."""
        if not self.items:
            print("Inventory is empty.")
            return
        print("\nCurrent Inventory:")
        for item in self.items:
            print(f"  {item}")
        print(f"Total inventory value: {self.total_inventory_value():.2f}\n")

    def save_to_file(self):
        """Writes all items to a plain text file, one per line."""
        with open(self.filename, "w") as f:
            for item in self.items:
                f.write(f"{item.name},{item.quantity},{item.price}\n")

    def load_from_file(self):
        """Loads items from the text file, if it exists."""
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    name, quantity, price = line.split(",")
                    self.items.append(Item(name, int(quantity), float(price)))
        except FileNotFoundError:
            # No saved data yet - start with an empty inventory.
            self.items = []


def main():
    inventory = Inventory()

    menu = (
        "\n--- Inventory Management System ---\n"
        "1. Add item\n"
        "2. Remove item\n"
        "3. Update item quantity\n"
        "4. Search item\n"
        "5. View all items\n"
        "6. Save and exit"
    )

    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            name = input("Item name: ").strip()
            try:
                quantity = int(input("Quantity: "))
                price = float(input("Price: "))
                inventory.add_item(name, quantity, price)
            except ValueError:
                print("Invalid input. Quantity must be a whole number and price a number.")

        elif choice == "2":
            name = input("Item name to remove: ").strip()
            inventory.remove_item(name)

        elif choice == "3":
            name = input("Item name: ").strip()
            try:
                new_quantity = int(input("New quantity: "))
                inventory.update_quantity(name, new_quantity)
            except ValueError:
                print("Invalid input. Quantity must be a whole number.")

        elif choice == "4":
            name = input("Item name to search: ").strip()
            item = inventory.find_item(name)
            print(item if item else f"'{name}' not found in inventory.")

        elif choice == "5":
            inventory.display_all()

        elif choice == "6":
            inventory.save_to_file()
            print("Inventory saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
