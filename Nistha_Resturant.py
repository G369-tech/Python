print("========== HariPrabodham ==========")
print("---------------------------------------")

# The Menu List
menu = {
    'Pizza' : 40,
    'Pasta' : 50,
    'Burger' : 60,
    'Salad' : 70,
    'Coffee' : 80,
}

print("=== Welcome to the Nistha Restaurant ===")  
print("Pizza : Rs40\nPasta : Rs50\nBurger : Rs60\nSalad : Rs70\nCoffee : Rs80")

order_total = 0
print("----------------------------------------------")
while True:
    item = input("Do you want to order something? Please enter the name of food from the given list ===> ").capitalize()
    if item in menu:
        order_total += menu[item]
        print(f'Your item {item} has been added to your order.')
    else:
        print(f"This {item} is not available. Please order from the given list.")
     
    user = input("Do you want to order another food item (y/n)? ")
    if user.lower() == 'n':
        break    
    print("----------------------------------------------")

print("----------------------------------------------")
print(f"The total amount of food is Rs{order_total}.")