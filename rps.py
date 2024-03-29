# This game was built using GitHub Copilot, but notably the code
# matches this website's version almost identically:
#   https://realpython.com/python-rock-paper-scissors/

import random
while true:
user_action = input ("input throw (rock, paper, scissors)or  'quit' to 'exit':  ").lower()
	if  user_action == 'quit':
	print("Thank you for playing! goodbye!")
	break

user_action = input("Enter throw (rock, paper, scissors): ")
ai_action = random.choice(["rock", "paper", "scissors"])

print(f"\nYou chose {user_action}, AI chose {ai_action}.\n")

if user_action == ai_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if ai_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
	if ai_action ="rock"://change the rock in place of paper to correct the code
        print("Paper covers rock! You win!")
	else:
	    print("scissor cuts paper! You lose.")
elif user_action == "scissors":
    if ai_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
play_again = input("Do you want to play again?  (yes/no): ")lower()
	if  play_again !=  'yes':
		print("Thanks for Playing ! Goodbye!")
		break
