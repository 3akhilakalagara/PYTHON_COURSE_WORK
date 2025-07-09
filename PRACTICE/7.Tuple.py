a = tuple() #empty tuple
b = (1, 2, 3) #tuple is immutable
c = ("apple", "banana", "cherry") #tuple with strings   
d = (1, "apple", 3.14, True) #mixed data types in a tuple
e = tuple(range(10)) #tuple with range of numbers from 0 to 9
print(e) # Output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Tuple Operations

# 1. Tuple Length
print(len(e)) # Output: 10

# 2. Tuple Indexing
print(e[5]) # Output: 5 (sixth element)

# 3. Tuple Slicing
print(b[1:4]) # Output: (2, 3) (elements from index 1 to 3)

#4. Tuple Concatenation
f = b + c # Concatenate two tuples  
print(f) # Output: (1, 2, 3, 'apple', 'banana', 'cherry')

# 5. Tuple Repetition
g = c * 2 # Repeat tuple c twice
print(g) # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# 6. Tuple Membership
print(2 in b) # Output: True (2 is in tuple b)
print("banana" in c) # Output: True (banana is in tuple c)

# 7. Tuple Methods

# a. count() - Count occurrences of an element
print(c.count("apple")) # Output: 1 (apple appears once in tuple c)

# b. index() - Find the index of the first occurrence of an element
print(c.index("banana")) # Output: 1 (banana is at index 1 in tuple c)

# c. max() - Find the maximum element in a tuple
print(max(e)) # Output: 9 (maximum value in tuple e)

# d. min() - Find the minimum element in a tuple
print(min(e)) # Output: 0 (minimum value in tuple e)

# e. sorted() - Return a sorted list from the tuple
print(sorted(c)) # Output: ['apple', 'banana', 'cherry'] (sorted list from tuple c)

# f. tuple() - Convert a list to a tuple
list_to_convert = [1, 2, 3]
converted_tuple = tuple(list_to_convert)
print(converted_tuple) # Output: (1, 2, 3)

# g. all() - Check if all elements in the tuple are true
print(all(e)) # Output: True (all elements in tuple e are non-zero) 

# h. any() - Check if any element in the tuple is true
print(any(e)) # Output: True (at least one element in tuple e is non-zero

# i. zip() - Combine two or more tuples into a single tuple of tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = tuple(zip(tuple1, tuple2))
print(zipped) # Output: ((1, 'a'), (2, 'b'), (3, 'c'))

