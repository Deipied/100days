#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
"""

print(logo)
import random
lives = 0
random_number = random.randint(1,100)
difficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    lives = 10
else:
    lives = 5
end_of_game = False

while not end_of_game:
    if lives == 0:
        end_of_game = True
    print(f"the asnwer is {random_number}")
    print(f"You have {lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess == random_number:
        end_of_game = True
        print(f"You got it! The answer was {random_number}")
    elif user_guess < random_number:
        print("Too low\nGuess again.")
        lives -= 1
    elif user_guess > random_number:
        print("Too high\nGuess again.")
        lives -= 1








