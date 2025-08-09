import programs as mp

while True:
    print("\n------ FUNCTION MENU ------")
    print("1. Multiplication Table")
    print("2. Simple Interest")
    print("3. Check Character Type")
    print("4. Reverse Number")
    print("5. ASCII Value")
    print("6. Current Date & Time")
    print("7. Vowel or Consonant")
    print("8. Replace Spaces with Hyphens")
    print("9. Pangram Check")
    print("10. Parallel Lines Check")
    print("0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        mp.multiplication_table()
    elif choice == "2":
        mp.simple_interest()
    elif choice == "3":
        mp.check_char_type()
    elif choice == "4":
        mp.reverse_number()
    elif choice == "5":
        mp.ascii_value()
    elif choice == "6":
        mp.current_datetime()
    elif choice == "7":
        mp.vowel_or_consonant()
    elif choice == "8":
        mp.replace_spaces()
    elif choice == "9":
        mp.pangram_check()
    elif choice == "10":
        mp.parallel_lines()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
