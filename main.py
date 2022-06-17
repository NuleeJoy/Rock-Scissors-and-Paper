from multiprocessing import RLock
import random

while True:

    user_action = input("Enter a choice (rock, paper, scissors); ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"/n You chose {user_action}, computer chose {computer_action}./n")


                #determining the winner
    if user_action == computer_action:
        print (f"Both players selected {user_action}. It's a tie!")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock smashes scissors, You win.")
        else:
            print("paper covers rock, You Lose.")


    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock, You win")
        else:
            print("scissors cuts paper, You Lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

    
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cuts paper, You Win")
    else:
        print("rock smashes scissors, You Lose")
