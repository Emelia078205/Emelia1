import sqlite3

def create_quiz():
    conn = sqlite3.connect("quiz_system.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        option_1 TEXT NOT NULL,
        option_2 TEXT NOT NULL,
        option_3 TEXT NOT NULL,
        option_4 TEXT NOT NULL,
        correct_answer TEXT NOT NULL)""")

    conn.commit()
    conn.close()

def add_question():
    conn = sqlite3.connect("quiz_system.db")
    cursor = conn.cursor()

    q_text = input("Enter the question:")
    op1 = input("Enter op1:")
    op2 = input("op2:")
    op3 = input("op3:")
    op4 = input("op4:")
    correct_answer = int(input("choose (1-4):"))

    cursor.execute("""INSERT INTO questions (question, option_1, option_2, option_3, option_4, correct_answer) VALUES (?,?,?,?,?,?)""",
    (q_text, op1, op2, op3, op4, correct_answer))

    conn.commit()
    conn.close()

def start_quiz():
    conn = sqlite3.connect("quiz_system.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()

    if not questions:
        print("there is no question added!")
        conn.close()
        return

    score = 0
    total_question = len(questions)

    for q in questions:
        print(f"Id:{q[0]}")
        print(f"Question:{q[1]}")
        print(f"1. {q[2]}")
        print(f"2. {q[3]}")
        print(f"3. {q[4]}")
        print(f"4. {q[5]}")

        user_answer = input("choose option(1-4):")

        if int(user_answer) == int(q[6]):
            print("Correct answer")
            score += 1
        else:
            print("Uncorrect answer")

    print(f"The final score is {score} ")
    conn.close()

def main_menu():
    while True:
        print("1. create_quiz_table")
        print("2. add_question")
        print("3. add quiz")
        print("4. Exsit")

        choice = input("Choose (1-4):")

        if choice == '1':
            create_quiz()
        elif choice == '2':
            add_question()
        elif choice == '3':
            start_quiz()
        elif choice == '4':
            break
        else:
            print("Plz choose a correct number next time<3!.")

if __name__ == "__main__":
    main_menu()
