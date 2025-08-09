def multiplication_table():
    print("Program: Multiplication Table")
    print(""" 
num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    """)
    print("Test Case 1: num=5 → 5x1=5 ... 5x10=50")
    print("Test Case 2: num=7 → 7x1=7 ... 7x10=70")
    print("Explanation: Loops from 1 to 10, multiplying the given number each time.")

def simple_interest():
    print("Program: Simple Interest")
    print("""
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time in years: "))
si = (p * r * t) / 100
print("Simple Interest =", si)
    """)
    print("Test Case 1: p=1000, r=5, t=2 → 100")
    print("Test Case 2: p=5000, r=7.5, t=1 → 375")
    print("Explanation: Formula SI = (P × R × T) / 100.")

def check_char_type():
    print("Program: Check if character is digit or alphabet")
    print("""
ch = input("Enter a character: ")
if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    print("Alphabet")
else:
    print("Special Character")
    """)
    print("Test Case 1: ch='A' → Alphabet")
    print("Test Case 2: ch='9' → Digit")
    print("Explanation: Uses str methods isdigit() and isalpha() to classify.")

def reverse_number():
    print("Program: Reverse a Number")
    print("""
n = int(input("Enter number: "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed:", rev)
    """)
    print("Test Case 1: n=123 → 321")
    print("Test Case 2: n=450 → 54")
    print("Explanation: Extracts digits and rebuilds number in reverse order.")

def ascii_value():
    print("Program: ASCII Value of Character")
    print("""
char = input("Enter character: ")
print("ASCII value of", char, "is", ord(char))
    """)
    print("Test Case 1: char='A' → 65")
    print("Test Case 2: char='a' → 97")
    print("Explanation: Uses ord() to get ASCII value.")

def current_datetime():
    print("Program: Current Date & Time")
    print("""
from datetime import datetime
now = datetime.now()
print("Current Date & Time:", now)
    """)
    print("Test Case: Prints current system date and time")
    print("Explanation: Uses datetime.now() to fetch current timestamp.")

def vowel_or_consonant():
    print("Program: Vowel or Consonant")
    print("""
ch = input("Enter a letter: ").lower()
if ch in 'aeiou':
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not a letter")
    """)
    print("Test Case 1: ch='E' → Vowel")
    print("Test Case 2: ch='b' → Consonant")
    print("Explanation: Checks membership in vowel set.")

def replace_spaces():
    print("Program: Replace spaces with hyphens")
    print("""
text = input("Enter string: ")
print(text.replace(" ", "-"))
    """)
    print("Test Case 1: 'Hello World' → 'Hello-World'")
    print("Test Case 2: 'Python is fun' → 'Python-is-fun'")
    print("Explanation: Uses replace() to swap spaces with hyphens.")

def pangram_check():
    print("Program: Pangram Check")
    print("""
import string
s = input("Enter text: ").lower()
if set(string.ascii_lowercase) <= set(s):
    print("Pangram")
else:
    print("Not Pangram")
    """)
    print("Test Case 1: 'The quick brown fox jumps over the lazy dog' → Pangram")
    print("Test Case 2: 'Hello world' → Not Pangram")
    print("Explanation: Checks if all alphabets exist in the string.")

def parallel_lines():
    print("Program: Parallel Lines Check (slopes)")
    print("""
m1 = float(input("Enter slope1: "))
m2 = float(input("Enter slope2: "))
if m1 == m2:
    print("Parallel")
else:
    print("Not Parallel")
    """)
    print("Test Case 1: m1=2, m2=2 → Parallel")
    print("Test Case 2: m1=1, m2=-1 → Not Parallel")
    print("Explanation: Lines are parallel if slopes are equal.")
