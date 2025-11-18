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

import random              # Imports the random module to allow the computer to make a choice
game_image=[rock,paper,scissors]

# Prompt the user for their choice and convert the input to an integer (0, 1, or 2)
your_turn=int(input("What do you want to choose?\n0=rock, 1=paper, 2=scissors :"))
print(game_image[your_turn])        # Display the user's chosen image/text based on their input number

computer_choice=random.randint(0,2)     # Generate a random integer (0, 1, or 2) for the computer's choice
print(f"computer choice is {computer_choice}")
print(game_image[computer_choice])

# --- Game Logic to Determine the Winner ---

if your_turn==computer_choice:         # Check for a draw (both players chose the same number)
    print ("its a draw!")
elif your_turn<0 or your_turn>2:       # Check if the user entered a number outside the valid range (0, 1, 2)
    print("invalid number you lose")
elif your_turn==2 and computer_choice==0:
    print("You lose ")
elif your_turn>computer_choice:
    print("You win!!")
elif computer_choice>your_turn:
    print("You lose!")
else:                                   # Fallback case 
    print("invalid number\n You lose")
    