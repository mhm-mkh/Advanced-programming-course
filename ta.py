def view_inventory(inventory):
    print(inventory)

def add_item(inventory, key, value):
    inventory[f"{key}"] = value

def remove_item(inventory, key):
    del inventory[key]

def update_inventory(inventory, key, value):
    inventory[f'{key}':value]

my_inventory = {"milk":5,
                "bread":6,
                "cheese":10}
while True:
    condition = False
    user_input_add = input("would you like to add an item?")
    if user_input_add == "yes" or user_input_add == "Yes":
        condition = True
        new_key = input("enter the items name")
        new_value = int(input("enter number of items"))
        add_item(my_inventory, new_key, new_value)
        view_inventory(my_inventory)
    user_input_remove = input("would you like to remove an item?")
    if user_input_remove == "yes" or user_input_remove == "Yes":
        condition = True
        new_key = input("enter the name of item you want to remove")
        remove_item(my_inventory, new_key)
        view_inventory(my_inventory)
    user_input_update = input("would you like to update an item value?")
    if user_input_update == "yes" or user_input_update == "Yes":
        condition = True
        key = input("please enter the name of the item")
        new_value = int(input("please enter updated value"))
        update_inventory(my_inventory, key, new_value)
        view_inventory(my_inventory)

    if condition is False:
        view_inventory(my_inventory)
        break
    

# view_inventory(my_inventory)
# add_item(my_inventory, "yogurt", 12)
# view_inventory(my_inventory)
# remove_item(my_inventory, "item2")
# view_inventory(my_inventory)
