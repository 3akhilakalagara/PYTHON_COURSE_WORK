#PURPLE(BEAUTY APP)

"""DATA TYPES"""

#str
product = input("Enter name of the product: ") #Enter name of the product: pilgrim face serum
print(f"Product: {product}") #Product: pilgrim face serum

#float
price = float(input("Enter the price of the product: ")) #Enter the price of the product: 699.80
print(f"Price: {price}") #Price: 699.80

#int
quantity = int(input("Enter the quantity of the product: ")) #Enter the quantity of the product: 1
print(f"Quantity: {quantity}") #Quantity: 1

#list
wishlist_items = list(map(str, input("Enter the items in your wishlist: ").split()))
print(f"Wishlist Items: {wishlist_items}") #Wishlist Items: ['serum', 'shampoo', 'conditioner']

#tuple
profile = tuple(map(str, input("Enter your profile details (name, email, phone): ").split()))
print(f"Profile: {profile}")
"""Enter your profile details (name, email, phone): akhila akhila@gmail.com 98765432
Profile: ('akhila', 'akhila@gmail.com', '98765432')"""

#set
categories = set(map(str, input("Enter the categories you browsed: ").split()))
print(f"Categories: {categories}")
"""Enter the categories you browsed: skincare makeup haircare
Categories: {'skincare', 'makeup', 'haircare'}"""

#dict
customer_preferences = eval(input("Enter your preferences: ")) 
print(f"Customer Preferences: {customer_preferences}")
"""Enter your preferences: {'skin type' : 'oily', 'brand':'pilgrim'}
Customer Preferences: {'skin type': 'oily', 'brand': 'pilgrim'}"""

#boolean
is_premium_member = True
print("Is Premium Member:", is_premium_member)# Is Premium Member: True

