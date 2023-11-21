
options = """Options:
1. Add item to the shopping list
2. View shopping list
3. Remove item from the shopping list
4. Quit
"""

shopping_list= []

while True:
    print(options)
    choice_num= int(input("Enter the number of your choice: "))
    if choice_num==1:
        add_item= input("Enter the item you want to add: ")
        shopping_list.append(add_item)
        print(f"{add_item} has been added to your shopping list.\n")

    elif choice_num==2:
        view_list=shopping_list()
        print("Your shopping list: \n")
        print(shopping_list) #still not working

    elif choice_num==3:
        remove= (input("Enter the item you want to remove:"))
        shopping_list.remove(remove)
        print(f"{remove} has been removed from your shopping list\n")
    elif choice_num==4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

