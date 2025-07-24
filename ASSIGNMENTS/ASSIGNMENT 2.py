#WHATS'APP CHAT DATA ANALYSIS

n = int(input("Enter number of messages: "))
chat = {}

for i in range(n):
    text = input()
    if ":" in text:
        name, message = text.split(":", 1)
        name = name.strip()
        message = message.strip()
        if name in chat:
            chat[name].append(message)
        else:
            chat[name] = [message]


while True:
    # Show menu to the user
    print("\nChoose an analysis option:")
    print("1. Count total number of messages")
    print("2. Identify unique users")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Find most frequent word by a user")
    print("9. First and last message by a user")
    print("10. Check if a user is in the chat")
    print("11. Find commonly repeated words")
    print("12. User with longest average message")
    print("13. Count messages mentioning a specific user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract all questions")
    print("17. Calculate reply ratio between two users")
    print("18. Check for deleted messages")
    print("19. Exit the program")

    # Ask for user's choice
    choice = input("Enter your choice (1-19): ")

    if choice == "1":
        count = 0
        for user in chat:
            count = count + len(chat[user])
        print(f"Count total number of messages:{count}")
    
    elif choice == "2":
        users = set(chat.keys())
        print(f"Identify unique users: {users}")

    elif choice == "3":
        words = 0  # Start from 0

        for person in chat:
            messages = chat[person]

            for one_msg in messages:
                word_list = one_msg.split()   
                word_count = len(word_list)   
                words = words + word_count  

        print(f"Count total words in the chat: {words}")

    elif choice == "4":
        if words>0:
            average = words/count
            print(f"Calculate average words per message:{average}")

    elif choice == "5":
            for person in chat:
              messages = chat[person]
              longest = max(messages, key=len)

            print(f"Longest message: {person}: {longest}")


    elif choice == "6":
        active = ""
        max_msgs = 0
        for person in chat:
              messages = chat[person]
              if len(messages) > max_msgs:
                  max_msgs = len(messages)
                  active = person
        print(f"Most active user:{active} ({max_msgs}messages)")

    elif choice == "7":
        name = input("Enter user_name: ")
        if name in chat:
            count = len(chat[name])
        print(f"Message sent by {name}:{count}")

    elif choice == "8":
        user = input("Enter user_name:")
        if user in chat:
            words = []
            for message in chat[user]:
                word = message.lower().split()
                words += word
            common = max(words, key=words.count)
        print(f"Most frequent word by {user}:{common}")

    elif choice == "9":
        name = input("Enter user_name:")
        if name in chat:
            messages = chat[name]
            if len(messages) > 1:
                first_msgs = messages[0]
                last_msgs = messages[-1]
        print(f'First message by {name}: "{name}: {first_msgs}" ')
        print(f'Last message by {name}: "{name}: {last_msgs}" ')
        

    elif choice == "10":
        name = input("Enter user_name:")
        if name in chat:
            print(f"{name} found in the chat")
        else:
            print(f"{name} is not found in the chat")

    elif choice == "11":
        all_words = []     
        repeated = []     
        for person in chat:
            for msg in chat[person]:
                words = msg.lower().split()      
                all_words += words               
        for word in all_words:
            if all_words.count(word) > 1 and word not in repeated:
                repeated.append(word)
        print(f"Common repeated words:{set(repeated)}")

            

    elif choice == "12":
        max_avg = 0
        max_user = ""
        for person in chat:
            messages = chat[person]
            total = 0
            for msgs in messages:
                total += len(msgs.split())
            avg = total / len(messages)
            if avg > max_avg:
                max_avg = avg
                max_user = person
        print(f"User with longest average message: {max_user} (avg{round(max_avg, 1)} words)")

    elif choice == "13":
        name = input("Enter user_name: ")
        count = 0
        for sender in chat:
            for msg in chat[sender]:
                words = msg.lower().split()
                if name in words:
                    count += 1
        print(f"Messages mentioning {name}:{count}")

    elif choice == "14":
        unique = set()
        for person in chat:
            for msg in chat[person]:
                unique.add(msg.strip())
        print(f"Unique messages count: {len(unique)}")
                

    
    elif choice == "15":
        all_messages = []

        for person in chat:
            for msg in chat[person]:
                all_messages.append(msg.strip())

        sorted_msgs = sorted(all_messages)

        print(sorted_msgs)

    elif choice == "16":
        for person in chat:
            for msg in chat[person]:
                if "?" in msg:
                    print(msg)
        else:
            print("no question in the chat")

    elif choice == "17":
        user1 = input("Enter 1st user name:")
        user2 = input("Enter 2nd user name:")
        count = 0
        if user2 in chat:
            for msg in chat[user2]:
                if user1.lower() in msg.lower():
                    count += 1
        print(f"Reply ratio from {user2} to {user1}: {count} replies")

    elif choice == "18":
        deleted = 0
        for person in chat:
            for message in chat[person]:
                cleaned = " ".join(message.strip().lower().split())
                if cleaned == "This message was deleted":
                    deleted += 1
        print(f"Deleted messages found: {deleted}")
        
    elif choice == "19":
        print("Exit the program")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 19.")
