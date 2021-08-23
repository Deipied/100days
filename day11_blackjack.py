logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
end_of_game = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
random_card = random.choice(cards)
your_cards = []
computer_cards = []
your_score = sum(your_cards)
computer_score = sum(computer_cards)


play_blackjack = input("Would you like to play a game of Blackjack? Type 'y' or 'n': ")

if play_blackjack == 'y':
      end_of_game = False

while end_of_game == True:
      play_blackjack = input("Would you like to play a game of Blackjack? Type 'y' or 'n': ")

def receive_card(x):
      x.append(random_card)

def check_score():
      global your_score
      global computer_score
      if your_score == 21 and computer_score < 10:
            print("BlackJack! You win!")
            end_of_game == True
      elif your_score > 21 and 11 in your_score:
            your_score -= 10
      elif computer_score > 21 and 11 in computer_score:
            computer_score -= 10
      elif your_score > 21:
            end_of_game == True
            end_of_game_calc()      


def current_standing():
      global your_score
      global computer_score
      print(f"Your cards: {your_cards}, current score: {your_score}\nComputer's first card: {computer_cards}")

def your_turn():
      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if another_card == 'y':
            receive_card(your_cards)
            check_score()
            your_turn()
      elif another_card == 'n':
            computer_turn()

def computer_turn():
      receive_card(computer_cards)
      check_score()
      if computer_score == 21:
            end_of_game = True
            end_of_game_calc()
      elif computer_score >= 17:
            end_of_game_calc()
      else:
            computer_turn()

while end_of_game == False:
      print(logo)
      receive_card(your_cards)
      receive_card(your_cards)
      receive_card(computer_cards)
      current_standing()
      check_score()
      your_turn()


def end_of_game_calc():
      print(f"Your final hand: {your_cards}, final score: {your_score}\nComputer's final hand: {computer_cards}, final score: {computer_score}")
      if your_score > 21:
            print("You lose!")
      elif computer_score > 21:
            print("You win!")
      elif your_score > computer_score:
            print("You win!")
      elif computer_score > your_score:
            print("You lose!")
      elif computer_score == your_score:
            print("Draw!")




            
      
      




############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
