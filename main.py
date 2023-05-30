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
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
else:
    print(scissors)

computer = random.randint(0,2)
print("conputer choose: \n")
if  computer == 0:
    print(rock)
elif  computer == 1:
    print(paper)
else:
    print(scissors)

if computer == user:
  print("Tie")
elif computer > user:
  print("Computer win")
elif computer == 0 and user == 2:
  print("Computer win")
else:
  print("You win")
