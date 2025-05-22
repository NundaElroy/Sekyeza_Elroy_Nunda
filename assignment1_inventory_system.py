#Inventory Management System

#initialize some sample inventory 
inventory = [
    {
    "name": "Laptop",
    "quantity" : 10,
    "price": 1200000
    },

    {
    "name": "Phone",
    "quantity" : 15,
    "price": 800000
    },

    {
    "name": "HeadPhones",
    "quantity" : 20,
    "price": 10000
    },

    {
    "name": "Charger",
    "quantity" : 30,
    "price": 5000
    }
]

# Main program loop
running = True
while running:
    # Display menu
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Display Inventory")
    print("2. Add New Item")
    print("3. Update Item Quantity")
    print("4. Update Item Price")
    print("5. Remove Item")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    # Option 1: Display Inventory
    if choice == '1':
        print("\n===== CURRENT INVENTORY =====")
        print("ID  | Name        | Quantity | Price")
        print("---------------------------------")

        for i, item in enumerate(inventory):
                print(f"{i}   | {item['name']:<12} | {item['quantity']:<8} | UGX {item['price']:<8}")
        
    # Option 2: Add New Item
    elif choice == '2':
       
        new_item = {}
        item_exists = False
       
        name = input("Enter item name: ")
        #chcking if an item exists
        for item in inventory:
            if item['name'].lower() == name.lower():
                item_exists = True
                break
            
        if item_exists:
            print(f"Item '{name}' already exists in inventory. ")
            continue
        else:
            valid_item = True
            new_item["name"] = name
        


       

        # Input validation for quantity
        valid_quantity = False
        while not valid_quantity:
            
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
            else:
                valid_quantity = True
                new_item["quantity"] = quantity

           
        
        # Input validation for price
        valid_price = False
        while not valid_price:
           
            price = int(input("Enter price: UGX "))
            if price < 0:
                print("Price cannot be negative. Please try again.")
            else:
                valid_price = True
                new_item["price"] = price
         
        
        # Add new item to inventory
        inventory.append(new_item)
        print(f"\n{name} added to inventory successfully!")
    
    # Option 3: Update Item Quantity
    elif choice == '3':
        # Display current inventory for reference
        print("\n===== CURRENT INVENTORY =====")
        print("ID  | Name        | Quantity | Price")
        print("---------------------------------")

        for i, item in enumerate(inventory):
                print(f"{i}   | {item['name']:<12} | {item['quantity']:<8} | UGX {item['price']:<8}")
        
        # Get item ID to update
        valid_id = False
        while not valid_id:
            
            item_id = int(input("\nEnter the ID of the item to update: "))
            if item_id < 0 or item_id >= len(inventory):
                print(f"Invalid ID. Please enter a number between 0 and {len(inventory) - 1}")
            else:
                valid_id = True
            
        
        # Get new quantity
        valid_quantity = False
        while not valid_quantity:
            try:
                new_quantity = int(input(f"Enter new quantity for {inventory[item_id]["name"]}: "))
                if new_quantity < 0:
                    print("Quantity cannot be negative. Please try again.")
                else:
                    valid_quantity = True
            except ValueError:
                print("Please enter a valid number.")
        
        # Update inventory
        inventory[item_id]["quantity"] = new_quantity
        print(f"\nQuantity for {inventory[item_id]["name"]} updated successfully!")


     # Option 3: Update Item Price
    elif choice == '4':
        # Display current inventory for reference
        print("\n===== CURRENT INVENTORY =====")
        print("ID  | Name        | Quantity | Price")
        print("---------------------------------")

        for i, item in enumerate(inventory):
                print(f"{i}   | {item['name']:<12} | {item['quantity']:<8} | UGX {item['price']:<8}")
        
        # Get item ID to update
        valid_id = False
        while not valid_id:
            
            item_id = int(input("\nEnter the ID of the item to update: "))
            if item_id < 0 or item_id >= len(inventory):
                print(f"Invalid ID. Please enter a number between 0 and {len(inventory) - 1}")
            else:
                valid_id = True
            
        
        # Get new quantity
        valid_price = False
        while not valid_price:
            try:
                new_price = int(input(f"Enter new price for {inventory[item_id]["name"]}: "))
                if new_price < 0:
                    print("price cannot be negative. Please try again.")
                else:
                    valid_price = True
            except ValueError:
                print("Please enter a valid number.")
        
        # Update inventory
        inventory[item_id]["price"] = new_price
        print(f"\nprice for {inventory[item_id]["name"]} updated successfully!")
    
    # Option 4: Remove Item
    elif choice == '5':
        # Display current inventory for reference
        print("\n===== CURRENT INVENTORY =====")
        print("ID  | Name        | Quantity | Price")
        print("---------------------------------")

        for i, item in enumerate(inventory):
                print(f"{i}   | {item['name']:<12} | {item['quantity']:<8} | UGX {item['price']:<8}")
        
        # Get item ID to remove
        valid_id = False
        while not valid_id:
           
            item_id = int(input("\nEnter the ID of the item to remove: "))
            if item_id < 0 or item_id >= len(inventory):
                print(f"Invalid ID. Please enter a number between 0 and {len(inventory) - 1}")
            else:
                valid_id = True
            
        
        # Remove item and confirm
        removed_item = inventory.pop(item_id)
        print(f"\n{removed_item["name"]} removed from inventory successfully!")
    
    # Option 5: Exit
    elif choice == '6':
        print("\nExiting program. Goodbye!")
        running = False
    
    # Invalid choice
    else:
        print("\nInvalid choice. Please try again.")