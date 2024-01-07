import random

def roll_dice():
    return random.randint(1, 6)

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"What is {num1} {operator} {num2}? "
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, answer

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        input("Press Enter to roll the dice or 'q' to quit: ")
        roll_result = roll_dice()
        print(f"You rolled: {roll_result}")
        
        if 1 <= roll_result <= 4:
            question, answer = generate_question()
            user_answer = input(question)
            try:
                user_answer = int(user_answer)
                if user_answer == answer:
                    print("Correct!")
                else:
                    print(f"Wrong! The correct answer is: {answer}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("You rolled outside the range. No question this time.")

        user_input = input("Roll again? (y/n): ").lower()
        if user_input != 'y':
            break

if __name__ == "__main__":
    main()
