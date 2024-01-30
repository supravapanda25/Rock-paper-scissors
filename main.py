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

image = [rock, paper, scissors]

you = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You chose:")
print(image[you])

computer = random.randint(0, 2)
print("Computer chose:")
print(image[computer])

if you >= 3 or you < 0: 
  print("You typed an invalid number, you lose!") 
elif you == 0 and computer == 2:
  print("CONGRATS, YOU WON!")
elif computer == 0 and you == 2:
  print("better luck next time:)")
elif computer > you:
  print("better luck next time:)")
elif you > computer:
  print("CONGRATS, YOU WON!")
elif computer == you:
  print("It's a draw")
