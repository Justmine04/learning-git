# Rock, paper, scissors

from os import system, name
from random import randint

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    
clear()
print("Welcom to The Rock Paper Scissor game")

choices = ["rock", "paper", "scissor"]
player_wins = 0
computer_wins = 0
while player_wins < 3 and computer_wins < 3:
    computer = (choices[randint(0,2)])

    player_choice = input("Make your choice: (q for quit) ").lower()
    if player_choice == "q":
        break
    if player_choice == computer:
        print("It's a draw")
    elif player_choice == "rock":
        if computer == "paper":
            print("Computer wins")
            computer_wins += 1
        else:
            print("You win")
            player_wins += 1
    elif player_choice == "paper":
        if computer == "scissor":
            print("Computer wins")
            computer_wins += 1
        else:
            print("You win")
            player_wins += 1
    elif player_choice == "scissors":
        if computer == "rock":
            print("Computer wins")
            computer_wins += 1
        else:
            print("You win")
            player_wins += 1
    print(f"Your score {player_wins}\nComputers score {computer_wins}")
if player_wins == 3:
    print("You won the whole game!")
elif computer_wins == 3:
    print("The computer won the whole game!")
else:
    print("Game stopped. Game over!")
