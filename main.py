import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

def player_choice():
    print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
    choice = int(input("Make your choice: "))
    if choice in [0, 1, 2]:
        print(options[choice])
        return choice
    else:
        print("Invalid choice. Please enter 0 for Rock, 1 for Paper, or 2 for Scissors.")
        return None

def computer_choice():
    comp_choice = random.randint(0, 2)
    print("Computer chose:\n")
    print(options[comp_choice])
    return comp_choice

def outcome(player, computer):
    if player is None:
        print("No valid choice made by the player.")
    elif player == computer:
        print("Draw!")
    elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("You win!")
    else:
        print("You lose!")

def main():
    player = player_choice()
    computer = computer_choice()
    outcome(player, computer)

main()