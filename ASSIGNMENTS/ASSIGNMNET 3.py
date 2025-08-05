# BUILD YOUR OWN QUIZ

questions = [
     "1. Which SQL command is used to retrieve data from a database? ",
     "2. Which of the following is a DDL command?",
     "3. Which clause is used with the SELECT statement to filter records based on a specified condition?",
     "4. Which of the following is used to uniquely identify each record in a table?",
     "5. Which SQL keyword is used to sort the result-set of a query?",
     "6. Which aggregate function calculates the average value of a numeric column?",
     "7. Which of the following is NOT a type of SQL JOIN?",
     "8. What does SQL stand for?",
     "9. Which command is used to remove all rows from a table without logging individual row deletions?",
     "10. Which constraint ensures that all values in a column are different?",
     "11. Which SQL statement is used to add new rows of data into a table?",
     "12. Which of the following is a DML command?",
     "13. What is the purpose of the LIKE operator in SQL?",
     "14. Which of the following is used to define a relationship between two tables?",
     "15. Which SQL statement is used to change existing data in a table?",
     "16. Which SQL constraint ensures that a column cannot have a NULL value?",
     "17. Which operator combines the result-set of two or more SELECT statements?",
     "18. What is the purpose of an index in a database?",
     "19. Which of the following is a TCL command?",
     "20.Which clause is used to group rows that have the same values in specified columns into a summary row?"
     ]


options = [
     ["A.UPDATE\nB.DELETE\nC.INSERT\nD.SELECT"],
     ["A.INSERT\nB.UPDATE\nC.CREATE\nD.SELECT"],
     ["A.GROUP BY\nB.ORDER BY\nC.WHERE\nD.HAVING"],
     ["A.Foreign Key\nB.Secondary Key\nC.Primary Key\nD.Candidate Key "],
     ["A.SORT BY\nB.ORDER BY\nC.ARRANGE BY\nD.GROUP BY"],
     ["A.SUM()\nB.COUNT()\nC.VAVG()\nD.MAX()"],
     ["A.INNER JOIN\nB.OUTER JOIN\nC.MIDDLE JOIN\nD.LEFT JOIN"],
     ["A.Standard Query Language\nB.Structured Question Language\nC.Structured Query Language\nD.Simple Query Logic"],
     ["A.DELETE\nB.DROP TABLE\nC.TRUNCATE TABLE\nD.REMOVE"],
     ["A.PRIMARY KEY\nB.FOREIGN KEY\nC.UNIQUE\nD.NOT NULL"],
     ["A.ADD INTO\nB.INSTER INTO\nC.CREATE ROW\nD.PUT DATA"],
     ["A.GRANT\nB.REVOKE\nC.UPDATE\nD.ALTER TABLE"],
     ["A.To compare exact values\nB.To perform pattern matching\nC.To join tables\nD.To sort data"],
     ["A.Primary Key\nB.Foreign Key\nC.Unique Key\nD.Candidate Key"],
     ["A.INSERT\nB.ALTER\nC.MODIFY\nD.UPDATE"],
     ["A.UNIQUE\nB.DEFAULT\nC.NOT NULL\nD.CHECK"],
     ["A.JOIN\nB.MERGE\nC.UNION\nD.COMBINE"],
     ["A.To increase data redundancy\nB.To improve the speed of data retrieval operations\nC. To enforce data integrity\nD.To secure data"],
     ["A.SELECT\nB.COMMIT\nC.CREATE\nD.INSERT"],
     ["A.WHERE\nB.ORDER BY\nC.HAVING\nD.GROUP BY"]
     ]

answers = ["D","C","C","C","B","C","C","C","C","C","B","C","B","B","D","C","C","B","B","D"]
guesses = []
score = 0
question_num = 0





for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your answer (A/B/C/D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("✔️  CORRECT!")
    else:
        print("✖️  INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    

print(f"🎯 Your score is: {score}/{len(questions)}")
print("ALL THE BEST")