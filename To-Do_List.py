print("====== Jay Swaminarayan =======")
print("-------------------------------")
print("=== HariPrabodham ===")
print("---------------------")
print("===== To-Do List =====")
print("----------------------")

my_list = []

print("===========")
print("Add for 1")
print("Edit for 2")
print("Delete for 3")
print("Display List for 4")
print("Exit for 0")
print("============")

while True:
    try:
        user = int(input("Enter Number: "))
        if user == 1:
            item = input("Enter item to add in list: ")
            my_list.append(item)
        elif user == 2:
            index_to_edit = int(input("Enter index to edit: "))
            new_value = input("Enter new value: ")
            if 0 <= index_to_edit < len(my_list):
                my_list[index_to_edit] = new_value
                print("Item at index", index_to_edit, "has been updated.")
            else:
                print("Index is out of range.")
        elif user == 3:
            d = input("Enter item to delete: ")
            if d in my_list:
                my_list.remove(d)
                print("Item deleted successfully.")
            else:
                print("Item not found in the list.")
        elif user == 4:
            print("===== List =====")
            for item in my_list:
                print(item)        
        elif user == 0:
            break
    except ValueError:
        print("Enter a valid input (integer).")