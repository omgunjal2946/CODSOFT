import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

print("Welcome to Rock-Paper-Scissors Game!")

while True:
    user_choice = input("Enter rock, paper or scissors (or 'quit' to stop): ").lower()
    if user_choice == 'quit':
        break

    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice, try again.")
        continue

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    print(get_winner(user_choice, computer_choice))
