import random

# Question Bank

unit_questions = [
    ("Convert 5 km to metres", "5000"),
    ("Convert 200 cm to metres", "2"),
    ("Convert 3 kg to grams", "3000"),
    ("Convert 120 minutes to hours", "2"),
    ("Convert 1.5 metres to cm", "150"),
]

general_questions = [
    ("What does CPU stand for?", "central processing unit"),
    ("What is the binary number for decimal 2?", "10"),
    ("What does RAM stand for?", "random access memory"),
    ("What does HTTP stand for?", "hypertext transfer protocol"),
    ("What is 8 x 7?", "56"),
]

# Defining Functions

def display_menu():
    print("\n Python Quiz App ===")
    print("1. Unit Conversion Quiz")
    print("2. General Knowledge Quiz")
    print("3. Exit")

def get_user_choice():
    return input("Select an option (1-3): ")

def ask_question(question, answer):
    user_answer = input(f"\n{question}\nYour answer: ").strip().lower()
    if user_answer == answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong! Correct answer: {answer}")
        return False

def run_quiz(question_list):
    score = 0
    random.shuffle(question_list)

    for q, a in question_list:
        if ask_question(q, a):
            score += 1

    print(f"\nFinal Score: {score}/{len(question_list)}")

def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "1":
            run_quiz(unit_questions)
        elif choice == "2":
            run_quiz(general_questions)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Program Start 

if __name__ == "__main__":
    main()
