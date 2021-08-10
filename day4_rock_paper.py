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
import random
computer_move = random.randint(0,2)
player_move = int(input("What do you choose? type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

def win():
  print('You win.')
def lose():
  print('You lose.')
def tie():
  print('You tie.')

if player_move == 0:
  print(rock)
  if computer_move == 0:
    print(f"Computer Chose:\n {rock}")
    tie()
  elif computer_move == 1:
    print(f"Computer Chose:\n {paper}")
    lose()
  else:
    print(f"Computer Chose:\n {scissors}")
    win()

if player_move == 1:
  print(paper)
  if computer_move == 0:
    print(f"Computer Chose:\n {rock}")
    win()
  elif computer_move == 1:
    print(f"Computer Chose:\n {paper}")
    tie()
  else:
    print(f"Computer Chose:\n {scissors}")
    lose()

if player_move == 2:
  print(scissors)
  if computer_move == 0:
    print(f"Computer Chose:\n {rock}")
    lose()
  elif computer_move == 1:
    print(f"Computer Chose:\n {paper}")
    win()
  else:
    print(f"Computer Chose:\n {scissors}")
    tie()
