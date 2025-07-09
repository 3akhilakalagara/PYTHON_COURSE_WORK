d = dict() #empty dictionary
d = {"name": "Rohit", "jersey": 45, "city": "Mumbai"} 
print(d) # Output: {'name': 'Rohit', 'jersey': 45, 'city': 'Mumbai'}

# Dictionary Operations

# 1. Dictionary Length
print(len(d)) # Output: 3 (three key-value pairs in the dictionary)

# 2. Dictionary Access
print(d["name"]) # Output: Rohit (access value by key)  
print(d.get("jersey")) # Output: 45 (access value using get method)

# 3. Dictionary Keys
print(d.keys()) # Output: dict_keys(['name', 'jersey', 'city'])

# 4. Dictionary Values
print(d.values()) # Output: dict_values(['Rohit', 45, 'Mumbai'])

# 5. Dictionary Items
print(d.items()) # Output: dict_items([('name', 'Rohit'), ('jersey', 45), ('city', 'Mumbai')])

# 6. Dictionary Membership
print("name" in d) # Output: True (key 'name' exists in dictionary)
print("age" in d) # Output: False (key 'age' does not exist in dictionary)

# 7. Dictionary Methods

# a. update() - Update dictionary with another dictionary or key-value pairs
d.update({"age": 30, "team": "India"})
print(d) # Output: {'name': 'Rohit', 'jersey': 45, 'city': 'Mumbai', 'age': 30, 'team': 'India'}

# b. pop() - Remove and return a value by key
removed_value = d.pop("city")
print(removed_value) # Output: Mumbai (value of removed key)
print(d) # Output: {'name': 'Rohit', 'jersey': 45, 'age': 30, 'team': 'India'}

# c. popitem() - Remove and return the last inserted key-value pair
last_item = d.popitem()
print(last_item) # Output: ('team', 'India') (last inserted key-value pair)
print(d) # Output: {'name': 'Rohit', 'jersey': 45, 'age': 30}

# d. clear() - Remove all items from the dictionary
d.clear()
print(d) # Output: {}

# e. copy() - Create a shallow copy of the dictionary
d_copy = d.copy()
print(d_copy) # Output: {}

# f. setdefault() - Get value by key, set default if key does not exist
d = {"name": "Rohit", "jersey": 45}
print(d.setdefault("age", 30)) # Output: 30 (sets default value)
print(d) # Output: {'name': 'Rohit', 'jersey': 45, 'age': 30}   

# g. delete - Remove a key-value pair by key
del d["age"]
print(d) # Output: {'name': 'Rohit', 'jersey': 45} (key 'age' removed)  