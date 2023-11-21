
options = """\nOptions:
1. Add item to the shopping list
2. View shopping list
3. Remove item from the shopping list
4. Quit"""

shopping_list= []

while True:
    print(options)
    choice_num= int(input("Enter the number of your choice: "))
    if choice_num==1:
        add_item= input("Enter the item you want to add: ").capitalize()
        shopping_list.append(add_item)
        print(f"{add_item} has been added to your shopping list.")

    elif choice_num==2:
        print("Your shopping list: ")
        for view_list in shopping_list:
            print(f"{view_list}")

    elif choice_num==3:
        remove= (input("Enter the item you want to remove: ")).capitalize()
        shopping_list.remove(remove)
        print(f"{remove} has been removed from your shopping list")

    elif choice_num==4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

