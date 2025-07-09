#1. String Concatenation
a = "akhila"
print("Hi " + a) #Hi akhila

#2. String Repetition
b = "Rohit"
print(b*3) #RohitRohitRohit

#3. Indexing
c = "Sharma"
print(c[2]) #a

#4. Slicing_[start:stop:step]
d = "Rohit Sharma"
print(d[0:5]) #Rohit [start:stop]
print(d[0:11:2])#RhtSam [start:stop:step]
print(d[:5])#Rohit [slice from the start]
print(d[0:])#Rohit Sharma [slice to the end]
print(d[:])#Rohit Sharma [slice whole string]
print(d[::2]) #RhtSam [slice whole string with step 2]
print(d[::-1]) #amrahS tihoR [reverse the string]
print(d[8:2:-1]) #ahS ti [start:end:-1, reverse slice between indices]

#Negative Slicing
x = "Rohit Sharma"
print(x[-4:-1]) #arm
print(x[::-1]) #amrahS tihoR
print(x[-1:-8:-1])#amrahS

#5. String Length
e = "Rohit Sharma"
print(len(e)) #12 [length of the string]

#6. String Methods
f = "Rohit Sharma"
print(f.upper()) #ROHIT SHARMA [convert to uppercase]
print(f.lower()) #rohit sharma [convert to lowercase]
print(f.title()) #Rohit Sharma [convert to title case]
print(f.split()) #['Rohit', 'Sharma'] [split into words]
print(f.find("Sharma")) #6 [find substring]
print(f.replace("Rohit", "Akhila")) #Akhila Sharma [replace substring]
print(f.startswith("Rohit")) #True [check if string starts with substring]
print(f.endswith("Sharma")) #True [check if string ends with substring]         
print(f.isalpha()) #False [check if all characters are alphabetic]
print(f.isalnum()) #False [check if all characters are alphanumeric]
print(f.isdigit()) #False [check if all characters are digits]
print(f.islower()) #False [check if all characters are lowercase]
print(f.isupper()) #False [check if all characters are uppercase]
print(f.isspace()) #False [check if all characters are whitespace]
print(f.strip()) #Rohit Sharma [remove leading and trailing whitespace]
print(f.lstrip()) #Rohit Sharma [remove leading whitespace]
print(f.rstrip()) #Rohit Sharma [remove trailing whitespace]
print(f.count("Rohit")) #1 [count occurrences of substring]
print(f.index("Sharma")) #6 [find index of substring]
print(f.capitalize()) #Rohit sharma [capitalize first letter]
print(f.swapcase()) #rOHIT sHARMA [swap case of all characters]
print(f.center(20, '*')) #****Rohit Sharma**** [center the string with padding]
print(f.zfill(20)) #0000000000Rohit Sharma [zero-fill the string to a specified width]
print(f.startswith("Rohit", 0, 5)) #True [check if string starts with substring in a specific range]
print(f.endswith("Sharma", 0, 12)) #True [check if string ends with substring in a specific range]

#7. String Formatting
name = "Akhila"
age = 21
print(f"My name is {name} and I am {age} years old.") #My name is Akhila and I am 21 years old.
print("My name is {} and I am {} years old.".format(name, age)) #My name is Akhila and I am 21 years old.
print("My name is %s and I am %d years old." % (name, age)) #My name is Akhila and I am 21 years old.
print("My name is {0} and I am {1} years old.".format(name, age)) #My name is Akhila and I am 21 years old.
print("My name is {name} and I am {age} years old.".format(name=name, age=age)) #My name is Akhila and I am 21 years old.

#8. Escape Characters
print("Hello\nWorld") #Hello    #World [newline]
print("Hello\tWorld") #Hello    World [tab]
print("Hello\\World") #Hello\World [backslash]
print("Hello\'World") #Hello'World [single quote]
print("Hello\"World") #Hello"World [double quote]