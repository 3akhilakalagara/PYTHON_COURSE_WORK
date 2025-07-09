s = set()
s = {1, 2, 3, 4, 5} 
print(s) # Output: {1, 2, 3, 4, 5}

# Set Operations

# 1. Set Length
print(len(s)) # Output: 5 

# 2. Set Membership
print(3 in s) # Output: True 
print(6 in s) # Output: False 

# 3. Set Union
s2 = {4, 5, 6, 7} # Another set
print(s.union(s2)) # Output: {1, 2, 3, 4, 5, 6, 7} (union of two sets)

# 4. Set Intersection
print(s.intersection(s2)) # Output: {4, 5} (common elements in both sets)

# 5. Set Difference
print(s.difference(s2)) # Output: {1, 2, 3} # Elements in s but not in s2

# 6. Set Symmetric Difference
print(s.symmetric_difference(s2)) # Output: {1, 2, 3, 6, 7} # Elements in either set but not both

# 7. Set Methods

# a. add() - Add an element to the set
s.add(6)
print(s) # Output: {1, 2, 3, 4, 5, 6} 

# b. remove() - Remove an element from the set (raises KeyError if not found)
s.remove(2)
print(s) # Output: {1, 3, 4, 5, 6} 

# c. discard() - Remove an element from the set (does not raise error if not found)
s.discard(10) # 10 is not in the set, no error raised
print(s) # Output: {1, 3, 4, 5, 6}

# d. pop() - Remove and return an arbitrary element from the set
removed_element = s.pop()
print(removed_element)
print(s) # Output: {3, 4, 5, 6} 

# e. clear() - Remove all elements from the set
s.clear()
print(s) # Output: set() 

# f. copy() - Create a shallow copy of the set
s_copy = s.copy()
print(s_copy) # Output: set() 

# g. union() - Return a new set with elements from both sets
s2 = {7, 8, 9}
s_union = s.union(s2)
print(s_union) # Output: {7, 8, 9} 

# h. intersection() - Return a new set with common elements from both sets
s3 = {8, 9, 10}
s_intersection = s.intersection(s3)
print(s_intersection) # Output: {8, 9} 

# i. difference() - Return a new set with elements in the first set but not in the second
s_difference = s.difference(s3)
print(s_difference) # Output: {1, 2, 3} 

# j. symmetric_difference() - Return a new set with elements in either set but not both
s_symmetric_difference = s.symmetric_difference(s3)
print(s_symmetric_difference) # Output: {1, 2, 3, 10} 

# k. update() - Update the set with elements from another set
s.update(s2)
print(s) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9} 
