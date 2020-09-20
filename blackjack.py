import random
import PySimpleGUI as sg
from random import *

def blackjack():
    import cards
    player_card1 = randint(1,11)
    player_card2 = randint(1,11)
    player_card3 = randint(1,11)
    dealer_card1 = randint(1,11)
    dealer_card2 = randint(1,11)
    add_player_cards = player_card1 + player_card2
    

    print("Your cards are: ", player_card1, " and ", player_card2, " with a total of: ", add_player_cards)
    user_input = input("\nWould you like to hit or stay: (hit/stay) ").lower()

    if (user_input == "hit"):
        new_player_value = player_card3 + add_player_cards
        while new_player_value <= 21:
            if (new_player_value == 21):
                replay1 = input("You won! Would you like to play again? (Y/N) ").lower()
                if (replay1 == 'y'):
                    blackjack()
                elif (replay1 == 'n'):
                    exit()
                else:
                    print("Invalid input")
            
        else:
            replay = input("Sorry! You busted, would you like to play again? (Y/N) ").lower()
            if (replay == 'y'):
                blackjack()
            elif (replay == 'n'):
                exit()
    elif (user_input == "stay"):
        print("placeholder")
blackjack()