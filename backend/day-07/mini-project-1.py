
options = """Options:
1. Add item to the shopping list
2. View shopping list
3. Remove item from the shopping list
4. Quit
"""

print(options)
shopping_list= [ ]

#Add an item Function
def option_1():
    add_item= input("Enter the item you want to add: ")
    shopping_list.append(add_item)
    print(f"{add_item} has been added to your shopping list.")

#Remove an Item Function
def option_3():
    remove= (input("Enter the item you want to remove:"))
    shopping_list.remove(remove)



choice_num= int(input("Enter the number of your choice: "))

while choice_num != 4:
    if choice_num==1:
        option_1
        
    elif choice_num==3:
        option_3

    else:
        print("Error")
print("Goodbye!")
