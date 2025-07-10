#PURPLE(BEAUTY APP)

"""DATA TYPES"""

# 1.integer
num_of_cart_items = 3

#2.float
total_order_value = 599.50

#3.string
customer_name = "Akhila"
address = "Ameerpet, Hyderabad"

#4.list[mutable]
cart_items = ["Plum Facewash", "Deconstruct Suncreen", "L'Oreal conditioner"]
wishlist_items = ["Mascara", "Lipstick", "Perfume"]

#5.tuple[immutable]
customer_info = ("Akhila", "akhilakalagara@gmail.com", "9876543210")

#6.dictionary[key:value pairs]
customer_preferences = {
    "skin_type": "oily",
    "preferred_brands": ["Plum", "Deconstruct", "L'Oreal"]
}

#7.set[unordered collection of unique items]
categories_browsed = {"skincare", "makeup", "haircare"}

#8.boolean
is_premium_member = True


print("Customer Name:", customer_name) #Customer Name: Akhila
print("Number of Cart Items:", num_of_cart_items)# Number of Cart Items: 3
print("Total Order Value:", total_order_value)# Total Order Value: 599.50
print("Shipping Address:", address)# Shipping Address: Ameerpet, Hyderabad
print("Cart Items:", cart_items)# Cart Items: ['Plum Facewash', 'Deconstruct Suncreen', "L'Oreal conditioner"]
print("Wishlist Items:", wishlist_items)# Wishlist Items: ['Mascara', 'Lipstick', 'Perfume']
print("Customer Info:", customer_info)# Customer Info: ('Akhila', 'akhilakalagara@gmail.com', '9876543210')
print("Customer Preferences:", customer_preferences)# Customer Preferences: {'skin_type': 'oily', 'preferred_brands': ["Plum", "Deconstruct", "L'Oreal"]}
print("Categories Browsed:", categories_browsed)# Categories Browsed: {'skincare', 'makeup', 'haircare'}
print("Is Premium Member:", is_premium_member)# Is Premium Member: True