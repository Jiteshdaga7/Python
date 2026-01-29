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
---'   ____)____
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

game_image = [rock, paper, scissors]

user_choice = int(input("What would you choose?\nPress 1 for rock, Press 2 for paper, Press 3 for scissors\n"))
#0, 1, 2
if user_choice >= 0 and user_choice < 2:
    print(game_image[user_choice])
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_image[computer_choice])
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid no. You Lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 1 and user_choice == 2:
    print("You Lose")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("It's a draw!")
