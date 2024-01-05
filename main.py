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
    if choice == 0:
        print(rock)
        """ return choice """
    elif choice == 1:
        print(paper)
        """ return choice """
    elif choice == 2:
        print(scissors)
        """ return choice """
    else:
        print("Invalid choice. Please enter 0 for Rock, 1 for Paper, or 2 for Scissors.")
    return choice

def computer_choice():
    comp_choice = random.randint(0, 2)
    print("Computer chose:\n")
    if comp_choice == 0:
        print(rock)
        """ return comp_choice """
    elif comp_choice == 1:
        print(paper)
        """ return comp_choice """
    elif comp_choice == 2:
        print(scissors)
    return comp_choice

def outcome():
    if player_choice() == 0 and computer_choice() == 2:
        print("You win!")
    elif player_choice() == 0 and computer_choice() == 1:
        print("You lose!")
    elif player_choice() == 0 and computer_choice() == 0:
        print("Draw!")

def main():
    player_choice()
    computer_choice()
    outcome()

main()