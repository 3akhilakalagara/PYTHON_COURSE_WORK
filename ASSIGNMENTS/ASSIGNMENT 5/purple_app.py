from purple_module import (
    NormalUser, PremiumUser, Payment,
    Haircare, Skincare, Makeup,
    SkincareRecommendation, MakeupRecommendation
)

print("----- Purple App OOP Implementation -----\n")

# Polymorphism: Choose User Type and Name
user_type = input("Enter user type (normal/premium): ").strip().lower()
if user_type == "premium":
    discount_percent = 20
elif user_type == "normal":
    discount_percent = 5
else:
    print("Invalid user type.")
    exit()
    

user_name = input("Enter user name: ").strip()




# Inheritance (Multi-level): Add Product Details
products = []
print("Add products (type 'stop' for product type to end):")
while True:
    prod_type = input("Product type (haircare/skincare/makeup): ").strip().lower()
    if prod_type == "stop":
        break
    name = input("Product name: ").strip()
    
    if prod_type == "haircare":
        hair_type = input("Hair type: ").strip()
        price = float(input("Price: "))
        product = Haircare(name, price, hair_type)
    elif prod_type == "skincare":
        skin_type = input("Skin type: ").strip()
        price = float(input("Price: "))
        product = Skincare(name, price, skin_type)  
    elif prod_type == "makeup":
        makeup_type = input("Makeup type: ").strip()
        price = float(input("Price: "))
        product = Makeup(name, price, makeup_type)
    else:
        print("Invalid product type, try again.")
        continue
    products.append(product)
    
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount
    print(f"Discount ({discount_percent}%): -₹{discount_amount:.2f}")
    print(f"Price after discount: ₹{final_price:.2f}\n")



# Encapsulation: Add Payment Methods
payment = Payment()
print("Add payment methods (card/online/cod). Type 'done' when finished:")


valid_modes = {"card","gpay","phnpay","paytym" "cod"}

while True:
    method = input("Enter payment method: ").strip().lower()
    if method == "done":
        break
    if method not in valid_modes:
        print("Invalid payment method.")
        continue
    payment.add_payment_details(method)

payment.show_payment_methods()
print()






# Abstraction: Display Recommendations
print("-- Personalized Recommendations --")
sc_rec = SkincareRecommendation()
mk_rec = MakeupRecommendation()

print(f"Skincare recommendations:\n{sc_rec.get_personalized_recommendations(user_name)}\n")
print(f"Makeup recommendations:\n{mk_rec.get_personalized_recommendations(user_name)}")
