import random
import os
from BlackJackUser import BlackjackUser as BlackJackUser

def display_cards_and_scores(user_player, computer_player, show_computer_cards=False): 
    if show_computer_cards != True:
        print(f"""
Your Cards: {user_player.cards}, and its score is {user_player.calculate_and_return_total_of_cards()}
Computer's first card: {computer_player.cards[1]}, and its score is {computer_player.calculate_and_return_total_of_cards()}
        """)
    else:
        print(f"""
Your final Cards: {user_player.cards}, and its score is {user_player.calculate_and_return_total_of_cards()}
Computer's final cards: {computer_player.cards}, and its score is {computer_player.calculate_and_return_total_of_cards()}
        """)
        
    
def play_blackjack():
    os.system('cls')
    
    user_player = BlackJackUser()
    computer_player = BlackJackUser()
    
    display_cards_and_scores(user_player, computer_player)
    
    cont = input("Type 'y' to get another card, type 'n' to pass\n")
    
    if cont.capitalize() == 'N':
        display_cards_and_scores(user_player, computer_player, show_computer_cards=True)
    else:
        user_player.cards.append(user_player.get_new_card())
        user_player.calculate_and_return_total_of_cards()
        if user_player.total_user_cards == 21:
            display_cards_and_scores(user_player, computer_player, show_computer_cards=True)
            print("You won!")
        # elif user_player.total_user_cards < 21:
            
#     play_again = input("Do you want to play again blackjack? Type 'y' or 'n': ")

    
        
play_blackjack()