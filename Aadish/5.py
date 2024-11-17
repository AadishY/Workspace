d = {}
a = "y"
while a == "y" or a == "Y" :
    p_name = input("Enter the product name: ")
    p_price = float(input("Enter product price: "))
    d[p_name] = p_price
    a = input("Do you want to enter more product names? (y/n): ")

a = "y"
while a == "y" or a == "Y" : 
    p_name = input("Enter the product name to search: ")
    print("Price:", d.get(p_name, "Product not found"))
    a = input("Do you want to know price of more products? (y/n): ")