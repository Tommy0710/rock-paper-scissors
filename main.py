
import random
user = int(input("What do you choose, 0 for ROCK, 1 for PAPER, 2 for Scissor: "))
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
if user >= 3 or user < 0:
  print("You chose wrong number, you lose")
else:
  print(f"Your choice: \n {game_image[user]}")

  computer = random.randint(0,2)
  print(f"Computer choice: \n{game_image[computer]}")
  
  if computer == user:
    print("Tie")
  elif computer > user:
    print("Computer win")
  elif computer == 0 and user == 2:
    print("Computer win")
  else:
    print("You win")

