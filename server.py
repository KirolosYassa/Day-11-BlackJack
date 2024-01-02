import random
import os
from BlackJackUser import BlackjackUser as BlackJackUser

def display_cards_and_scores(user_player, computer_player, show_computer_cards=False): 
    if show_computer_cards != True:
        print(f"""
Your Cards: {list(user_player.cards)}, and its score is {user_player.calculate_and_return_total_of_cards()}
Computer's first card: {list(computer_player.cards)[1]}, and its score is {list(computer_player.cards)[1]}
        """)
    else:
        print(f"""
Your final Cards: {list(user_player.cards)}, and its score is {user_player.calculate_and_return_total_of_cards()}
Computer's final cards: {list(computer_player.cards)} and its score is {computer_player.calculate_and_return_total_of_cards()}
        """)
        
    
def play_blackjack():
    os.system('cls')
    
    
    user_player = BlackJackUser()
    computer_player = BlackJackUser()
    
    def computer_turn():
        display_cards_and_scores(user_player, computer_player, show_computer_cards=True)
        
        # user_player.cards.append(user_player.get_new_card())
        # if user_player.lost_or_not_yet():
        count = random.randint(1, 5)
        user_player.calculate_and_return_total_of_cards()
        for i in range(count):
            computer_player.cards.append(computer_player.get_new_card())
            computer_player.calculate_and_return_total_of_cards()
            
            
            if computer_player.total_user_cards == 21:
                print("So this is the BlackJack!")
            
            if computer_player.total_user_cards > user_player.total_user_cards:
                print("You Lost")
            elif computer_player.total_user_cards == user_player.total_user_cards:
                print("Draw!")
            elif computer_player.total_user_cards > 21 and user_player.total_user_cards >= 21:
                print("You Lost")
            elif computer_player.total_user_cards > 21 and user_player.total_user_cards <= 21:
                print("You win!")
        
        user_player.calculate_and_return_total_of_cards()
        computer_player.calculate_and_return_total_of_cards()
    
    def game_continue():
            
        display_cards_and_scores(user_player, computer_player)
        
        cont = input("Type 'y' to get another card, type 'n' to pass\n")
        
        if cont.capitalize() == 'N':
            computer_turn()
                
        else:
            user_player.cards.append(user_player.get_new_card())
            
            if user_player.lost_or_not_yet():
                display_cards_and_scores(user_player, computer_player)
                print("Busted!")
                computer_turn()
                
            #     for i in range(random.randint(1, 5)):
            #         computer_player.cards.append(computer_player.get_new_card())
            #         user_player.calculate_and_return_total_of_cards()
            #         computer_player.calculate_and_return_total_of_cards()
                    
                    
            #         if computer_player.total_user_cards == 21:
            #             print("So this is the BlackJack!")
                    
            #         if computer_player.total_user_cards > user_player.total_user_cards:
            #             print("You Lost")
            #         elif computer_player.total_user_cards == user_player.total_user_cards:
            #             print("Draw!")
            #         elif computer_player.total_user_cards > 21 and user_player.total_user_cards >= 21:
            #             print("You Lost")
            #         elif computer_player.total_user_cards > 21 and user_player.total_user_cards <= 21:
            #             print("You win!")
                        
            
            game_continue()
                
    game_continue()
        
#     play_again = input("Do you want to play again blackjack? Type 'y' or 'n': ")

    
        
play_blackjack()