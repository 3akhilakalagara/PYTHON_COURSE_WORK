
#1. Check if three lengths form an Equilateral, Isosceles, or Scalene triangle

a,b,c = tuple(map(int,input().split()))
if a==b and b==c and a==c:
  print("Equilateral")
elif a == b or b==c or a==c:
  print("Isosceles")
else:
  print("Scalene")

#2. Classify a character as: vowel, consonant, digit, special character

a = input()
v = "aeiouAEIOU"
for i in v:
  if a == i:
    print("Vowel")
    break
else:
    print("Special Character")

#3. BMI Calculator and Category

h,w = tuple(map(float, input().split()))
bmi = w/h*h
if bmi < 18.5:
  print("Underweight")
elif 18.5 <= bmi <= 24.9:
  print("Normal weight")
elif 25<=bmi<=29.9:
  print("Overweight")
elif bmi>=30:
  print("Obesity")

#4. Electricity bill calculator based on units used

n = int(input())

bill= 0

if 0<=n<=50 :
  bill = n*1
  print(bill)

elif 101<=n<=200:
  bill = 50*1 + (n-50)*2
  print(bill)

elif n > 201:
  bill = 50*1 + 100*2 + (n-150)*3
  print(bill)

#5. Check if a number is Armstrong (3-digit)
n = input()
a = (int(n[0])**3 + int(n[1])**3 + int(n[2])**3)
if str(a) == n:
  print("Armstrong")
else:
  print("Not Armstrong")

#6. Validate strong password (min 8 chars, 1 uppercase, 1 digit, 1 special char)

n = input()
if len(n) >= 8:
  upper = False
  digit = False
  special = False

  for i in n:
    if i.isupper():
      upper = True
    elif i.isdigit():
      digit = True
    elif i in "!@#$%^&*":
      special = True

  if upper and digit and special:
    print("Strong Password")
  else:
    print("Invalid Password")
else:
  print("Invalid Password")

#7. ATM Withdrawal Simulation

balance, withdraw = list(map(int,input().split()))

if withdraw >= 500:
  if withdraw%100==0:
    if withdraw <= balance:
      print("Success")
    else:
      print("Insufficient Balance")
  else:
    print("Invalid Amount")
else:
  print("Invalid Amount")

#8. Ticket fare calculator with age-based discounts

age = int(input())

if age < 5:
  print("Free")
elif age<18:
  print(100-(100*50/100))
elif age > 60:
  print(100-(100*30/100))

#9. 24-hour to 12-hour time converter

hr,min = tuple(map(int,input().split(":")))

if 0<=hr<=23 and 0<=min<=60:
  if 0<=hr<=12:
    print(f"{hr}:{min} AM")
  elif 13<=hr<=23:
    print(f"{hr}:{min} PM")
  else:
    print("Invalid Time")

#10. Find category of a character based on ASCII range
"""
Uppercase Alphabet → ASCII 65–90

Lowercase Alphabet → ASCII 97–122

Digit → ASCII 48–57

"""

n = input()
if len(n) == 1:
  asci = ord(n)
  if 65<=asci<=90:
    print("Uppercase Alphabet")
  elif 97<=asci<=122:
    print("Lowercase Alphabet")
  elif 48<=asci<=57:
    print("Digit")
  else:
    print("Special Character")
else:
  print("Invalid input")

#11. Grading system with nested bands (including + and - grades)
"""
Question:
● 90–100: A
● 85–89: B+
● 80–84: B
● 70–79: C
● Below 70: F
"""

n = int(input())
if 90<=n<=100:
  print("A")
elif 85<=n<=89:
  print("B+")
elif 80<=n<=84:
  print("B")
elif 70<=n<=79:
  print("C")
elif n<70:
  print("F")

#12. Currency denomination counter
#Question: Input amount. Return number of 2000s, 500s, 100s, etc.

n = int(input())
n_2k = n//2000
n = n%2000
n_500 = n//500
n = n%500
n_100 = n//100
n = n%100
print(f"2000's : {n_2k}\n500's : {n_500}\n100's : {n_100}")

"""
or

countof2k=0
while money>=2000:
  money-=2000
  countof2k+=1

print(f'{countof2k}*2000')

countof500=0
while money>=500:
  money-=500
  countof500+=1

print(f'{countof500}*500')

"""

#13. Movie ticket price based on day and age
"""Question:
● Weekends: ₹200
● Weekdays: ₹150
● Children < 12: 50% discount"""

age = int(input())
day = input().lower()
if age<=12:
  if day == "sunday" or day == "saturday":
    print(200-(200*50/100))
  else:
    print(150-(150*50/100))
elif age>12:
  if day == "sunday" or day == "saturday":
    print("₹200")
  else:
    print("₹150")

#14. Classify angle as Acute, Right, Obtuse, Straight

angle = int(input())
if angle < 90:
  print("Acute")
elif angle == 90:
  print("Right")
elif 90<angle<180:
  print("Obtuse")
elif angle == 180:
  print("Straight")

#15. Grade college admission based on marks in 3 subjects
"""Question: If average > 90 and each subject > 70 → Admit
Else if average > 80 → Waitlist
Else → Reject"""


s1,s2,s3 = list(map(int,input().split()))
avg = (s1+s2+s3)/3
if s1>70 and s2>70 and s3>70 and avg>90:
  print("Admit")
elif avg > 80:
  print("Waitlist")
else:
  print("Reject")

#16. Check if a number is perfect
"""Question: A number is perfect if the sum of its divisors equals the number itself. Write a
program to check this."""

n = int(input())
a = []
if n>0:
  for i in range(1,n):
    if n%i== 0:
      a.append(i)
  if sum(a) == n:
      print("Perfect number")
  else:
      print("Not perfect")

else:
  print("Invalid number")

#17. Identify type of triangle by angles
#Question: Input 3 angles and determine if the triangle is acute, right, or obtuse


angle = int(input())
if angle <90:
  print("acute")
elif angle == 90:
  print("right")
elif 90<angle<180:
  print("obtuse")

#18. Convert marks (0–100) to 10-point GPA scale
"""Question: Write rules to map:
● 91–100: 10
● 81–90: 9
● 71–80: 8"""

marks = int(input())
if 0<marks<100:
  if 91<=marks<=100:
    print(10)
  elif 81<=marks<=90:
    print(9)
  elif 71<=marks<=80:
    print(8)
  elif 61<=marks<=70:
    print(7)
  elif 51<=marks<=60:
    print(6)
  else:
    print("fail")

#19. Check if four digits form a lucky number (sum of first two == last two)

n = input()
if int(n[0]) + int(n[1]) == int(n[2]) + int(n[3]):
  print("Lucky number")
else:
  print("Not lucky number")

#20. Car insurance premium based on age and experience
"""Question:
● Age < 25 and experience < 3 → High risk
● Age > 25 and experience > 5 → Low risk"""


age = int(input())
experience = int(input())
if age < 25 and experience < 3:
  print("High risk")
elif age > 25 and experience > 5:
  print("Low risk")
else:
  print("Medium risk")

#21. Ticket system for amusement park
"""Question:
● Children < 12: ₹50
● Adults < 60: ₹100
● Senior: ₹60"""

age = int(input())
if age < 12:
  print("₹50")
elif age <60:
  print("₹100")
elif age >=60:
  print("₹60")

#22. Classify number as Single, Double, or Triple digit

n = int(input())
if 0<=n<=9:
  print("Single digit")
elif 10<=n<=99:
  print("Double digit")
elif 100<=n<=999:
  print("Triple digit")

#23. Validate time input (HH:MM format)
#Question: Ensure 0 <= HH <= 23 and 0 <= MM <= 59

h,m = list(map(int,input().split(":")))
if 0<=h<=23 and 0<=m<=59:
  print("valid")
else:
  print("invalid")

#24. Weather categorization by temperature
"""Question:
● < 10: Very Cold
● 10–20: Cold
● 21–30: Warm
● 30: Hot"""


temp = int(input())
if temp<10:
  print("very cold")
elif 10<=temp<=20:
  print("cold")
elif 21<=temp<=30:
  print("warm")
elif temp>30:
  print("Hot")

#25. Assign mobile plan based on usage
"""Question:
● < 1GB: Plan A
● < 5GB: Plan B
● 5GB: Plan C"""

n = float(input())
if n<1:
  print("plan A")
elif 1<=n<5:
  print("plan B")
elif n>=5:
  print("plan C")

#26. Identify duplicate digits in a 3-digit number

n = input()
for i in n:
  if n.count(i) > 1:
    print("duplicate")
    break
else:
  print("no duplicate")

#27. Weekday classifier (Input: 1–7, Output: Day type)

n = int(input())

if 1<=n<=5:
  print("weekday")
elif n == 6 or n==7:
  print("weekend")

#28. Student attendance eligibility (> 75% to write exam)

n = int(input())
if 75<=n<=100:
  print("eligible")
elif n<=60:
  print("not eligible")

#29. Print grade trend based on increasing or decreasing scores
#Question: Take three test scores and tell if improving, declining or fluctuating.

t1,t2,t3 = list(map(int,input().split()))
if t1<t2 and t2<t3:
  print("improving")
elif t1<t2 and t2>t3:
  print("fluctuating")
elif t1>t2 and t2>t3:
  print("declining")

#30. Validate mobile number (10 digits, starts with 6–9)

p = input()
if len(p) == 10:
  if p.startswith("6") or p.startswith("7") or p.startswith("8") or p.startswith("9"):
    print("valid")
  else:
    print("invalid")
else:
  print("invalid")