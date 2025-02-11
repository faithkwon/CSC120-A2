from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory:List[Computer]):
        self.inventory = inventory

    # What methods will you need?

    # Buys the computer (adds it to the inventory)
    def buy(self, new_comp:Computer):
        self.inventory.append(new_comp) # adds new computer to inventory
    
    # Sells the computer (removes it from the inventory)
    def sell(self, item_id:int):
        old_item = self.inventory[item_id]
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id) # removes computer from inventory
            print("Item", old_item.description, "sold!")
        else:
            print("Item", self.inventory[item_id].description, "not found. Please select another item to sell.")

    # Updates the price of the computer
    def update_comp_price(self, item_id:int, new_price:int):
        if self.inventory[item_id] is not None:
            self.inventory[item_id].update_price(new_price) # updates price 
            print("Item", self.inventory[item_id].description, "is now $", new_price)
        else:
            print("Item", self.inventory[item_id].description, "not found. Cannot update price.")

    # Refurbishes the computer
    def refurbish_comp(self, item_id:int, new_os:Optional[str] = None):
        if self.inventory[item_id] is not None:
            self.inventory[item_id].refurbish(new_os) # updates OS
        else:
            print("Item", self.inventory[item_id].description, "not found. Cannot refurbish.")
        
    # Prints the current inventory
    def print_inventory(self):
        if not self.inventory:
            print("The inventory is currently empty.")
        else:
            for i in self.inventory:
                # Print its details
                print(f"Description: {i.description}, Processor: {i.processor_type}, Memory: {i.memory} GB, OS: {i.operating_system}, Year: {i.year_made}, Price: ${i.price}")


# Sample main method to test program
def main():
    computer1 = Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
    computer2 = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 15000) 

    shop = ResaleShop([])

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer1.description)
    print("Adding to inventory...")
    shop.buy(computer1)
    print("Done.\n")

    # Add another computer to the resale store's inventory
    print("Buying", computer2.description)
    print("Adding to inventory...")
    shop.buy(computer2)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    print("Refurbishing Item:", computer1.description, ", updating OS to 'MacOS Monterey'.")
    print("Updating inventory...")
    shop.refurbish_comp(0, "MacOS Monterey")
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item:", computer1.description)
    shop.sell(0)

    # Changing the price of the other computer
    new_price = 1000
    print("Changing price of:", computer2.description, "to $", new_price)
    shop.update_comp_price(0, new_price)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
if __name__ == "__main__":
    main()