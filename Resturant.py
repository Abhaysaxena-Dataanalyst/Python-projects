menu = {
    'pizza': 199,
    'Burger': 40,
    'Noddles': 40,
    'Veg Momos': 30,
    'Chicken Momos': 50,
}

print("Welcomee to Saxena's Kitchen")
print('pizza: 199\nBurger: 40\nNoddles: 40,\nVeg Momos: 30\nChicken Momos: 50')

order_total = 0

while True:
    item = input("Enter the dish name you want to try? = ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} is added here and your order total for this {order_total}")
    else:
     print(f"Sorry we don't have {item} right now")

    another_order = input("Would you like to add anything else as well (yes/no): ")
    if another_order.lower() !='yes':
          break
name= input("Please enter your Good name: ")
Address= input("Please enter youur address for Delivery: ")
phone__no = int(input("Enter our activate Phone number: "))
print("-----------------------------------------------------------------------------------------")
print(f"Here's you bill Mr.{name}")
print("Name" ,name)
print("Phone number", phone__no)
print("Address", Address)
print(f"Your order total is= {order_total}")
print("-----------------------------------------------------------------------------------------")
