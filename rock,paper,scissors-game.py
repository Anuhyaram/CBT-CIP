import random

def get_computer_choice():
    choices = ["software engineer", "singer"]
    return random.choice(choices)

def get_user_choice():
    choice = input("Enter your choice (software engineer or singer): ").lower()
    while choice not in ["software engineer", "singer"]:
        choice = input("Invalid choice. Enter software engineer or singer: ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "software engineer" and computer_choice == "singer") or \
         (user_choice == "singer" and computer_choice == "software engineer"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Software Engineer vs. Singer!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")

if _name_ == "_main_":
    play_game()
