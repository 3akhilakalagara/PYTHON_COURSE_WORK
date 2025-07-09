a = list() # Empty list
b = [1, 2, 3, 4, 5] # List with integers
c = ["apple", "banana", "cherry"] # List with strings   
d = [1, "apple", 3.14, True] # Mixed data types in a list
e = list(range(10)) # List with range of numbers from 0 to 9
print(e) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# List Operations

# 1. List Length
print(len(e)) # Output: 10

# 2. List Indexing
print(e[5]) # Output: 5 (sixth element)

# 3. List Slicing
print(b[1:4]) # Output: [2, 3, 4] (elements from index 1 to 3)
print(c[:2]) # Output: ['apple', 'banana'] (first two elements) 
print(d[1:]) # Output: ['apple', 3.14, True] (selements from index 1 to end)
print(e[::2]) # Output: [0, 2, 4, 6, 8] (every second element)
print(e[::-1]) # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed list)

# 4. List Concatenation
f = b + c # Concatenate two lists   
print(f) # Output: [1, 2, 3, 4, 5, 'apple', 'banana', 'cherry']

# 5. List Repetition
g = c * 2 # Repeat list c twice
print(g) # Output: ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']

# 6. List Membership
print(2 in b) # Output: True (2 is in list b)
print("banana" in c) # Output: True (banana is in list c)
print(3.14 in d) # Output: True (3.14 is in list d)
print(10 in e) # Output: False (10 is not in list e)

# 7. List Methods

# a. append() - Add an element to the end of the list
d.append("orange")
print(d) # Output: [1, "apple", 3.14, True, "orange"]

# b. extend() - Add multiple elements to the end of the list
d.extend(["grape", "kiwi"])
print(d) # Output: [1, "apple", 3.14, True, "orange", "grape", "kiwi"]  

# c. insert() - Insert an element at a specific index
d.insert(1, "mango")
print(d) # Output: [1, "mango", "apple", 3.14, True, "orange", "grape", "kiwi"]

# d. remove() - Remove the first occurrence of an element
d.remove("apple")
print(d) # Output: [1, "mango", 3.14, True, "orange", "grape", "kiwi"]

# e. pop() - Remove and return an element at a specific index (default is the last element)
removed_element = d.pop()
print(removed_element) # Output: kiwi
print(d) # Output: [1, "mango", 3.14, True, "orange", "grape"]

# f. clear() - Remove all elements from the list
d.clear()
print(d) # Output: []

# g. index() - Find the index of the first occurrence of an element
d = ["apple", "banana", "cherry"]
print(d.index("banana")) # Output: 1 (index of "banana")

# h. count() - Count the occurrences of an element in the list
print(d.count("orange")) # Output: 0 (orange is not in the list)

# i. sort() - Sort the list in ascending order (for numbers) or alphabetical order (for strings)
h = [3, 1, 4, 2]
h.sort()
print(h) # Output: [1, 2, 3, 4]

# j. reverse() - Reverse the order of elements in the list
h.reverse()
print(h) # Output: [4, 3, 2, 1] 

# k. copy() - Create a shallow copy of the list
i = h.copy()
print(i) # Output: [4, 3, 2, 1]

# l. join() - Join elements of a list into a string (only for strings)
j = ["Hello", "World"]
print(" ".join(j)) # Output: Hello World    

# m. split() - Split a string into a list (only for strings)
k = "Python is fun"
print(k.split()) # Output: ['Python', 'is', 'fun']  

# n. min() - Find the minimum element in a list
print(min(h)) # Output: 1 (minimum element in list h)   

# o. max() - Find the maximum element in a list
print(max(h)) # Output: 4 (maximum element in list h)

# p. sum() - Calculate the sum of elements in a list (only for numbers)
print(sum(h)) # Output: 10 (sum of elements in list h)

# q. any() - Check if any element in the list is True (or non-zero)
print(any([0, 0, 1])) # Output: True (1 is True)
print(any([0, 0, 0])) # Output: False (all are False

# r. all() - Check if all elements in the list are True (or non-zero)
print(all([1, 2, 3])) # Output: True (all are non-zero)
print(all([1, 0, 3])) # Output: False (0 is False)

# s. zip() - Combine two or more lists into a list of tuples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped)) # Output: [(1, 'a'), (2, 'b'), (3, 'c')]