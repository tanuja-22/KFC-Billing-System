import time
import random

class KFCBillingCounter:
    def __init__(self):
        self.menu = {
            'Chicken Burger': 5.00,
            'Veg Burger': 4.50,
            'Fries': 2.00,
            'Coke': 1.50,
            'Pepsi': 1.50,
            'Chicken Wings': 6.00,
            'Chicken Popcorn': 4.00,
        }
        self.order = {}
        self.token_number = random.randint(1000, 9999)
        self.counter_number = random.randint(1, 5)

    def display_menu(self):
        print("\nKFC Menu:")
        for item, price in self.menu.items():
            # Display each price formatted to two decimal places
            print(f"{item}: ${price:.2f}")
        print("\n")

    def take_order(self):
        while True:
            self.display_menu()
            item = input("Enter the item you want to order (or 'done' to finish): ").strip()
            if item.lower() == 'done':
                break
            elif item in self.menu:
                quantity = int(input(f"How many {item} do you want? "))
                if item in self.order:
                    self.order[item] += quantity
                else:
                    self.order[item] = quantity
            else:
                print("Item not found in the menu. Please try again.")

    def calculate_total(self):
        total = 0
        for item, quantity in self.order.items():
            total += self.menu[item] * quantity
        return total

    def generate_bill(self):
        print("\nYour Bill:")
        for item, quantity in self.order.items():
            # Display each line in the bill formatted to two decimal places
            item_total = self.menu[item] * quantity
            print(f"{item}: {quantity} x ${self.menu[item]:.2f} = ${item_total:.2f}")
        
        total = self.calculate_total()
        print(f"\nTotal: ${total:.2f}")
        print(f"Token Number: {self.token_number}")
        print(f"Please collect your order at counter number {self.counter_number}.\n")

    def process_order(self):
        print("\nThank you for your order. Please wait while we process your order...")
        # Simulating order processing time
        time.sleep(3)
        print("Your order is ready! Please collect it at the counter.")

if __name__ == "__main__":
    counter = KFCBillingCounter()
    counter.take_order()
    counter.process_order()
    counter.generate_bill()

    