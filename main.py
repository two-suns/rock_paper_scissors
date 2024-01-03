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
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)
    else:
        print("Invalid choice. Please enter 0 for Rock, 1 for Paper, or 2 for Scissors.")

def main():
    player_choice()

main()