#variable declaration and importing 
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TEST CASE
print(chosen_word)

# Creating blanks based on word_length
display = []
for _ in range(word_length):
    display += "_"


# while loop for guesses/the game
lives = 6
while not end_of_game:
    guess = input("Guess a letter:").lower()
    for index in range(word_length):
        letter = chosen_word[index]
        # print(f"Current position: {index}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[index] = letter
        else:
            lives -= 1    
            print(lives)
            print(stages[lives])

    print(f"{' '.join(display)}")
    if lives == 0:
        end_of_game = True
        print(f"You lose, the word was {chosen_word}.")

    if "_" not in display:
        end_of_game = True
        print("CONGRATS YOU WON")