import random
import os
from BlackJackUser import BlackjackUser as BlackJackUser
import time



def display_cards_and_scores(user_player, computer_player, show_computer_cards=False):
    user_player.calculate_and_return_total_of_cards() 
    computer_player.calculate_and_return_total_of_cards() 
    if show_computer_cards != True:
        return f"""
Your Cards: {list(user_player.cards)}, and its score is {user_player.total_user_cards}
Computer's first card: {computer_player.get_only_first_card()}, and its score is {computer_player.get_total_cards_with_first_element_only()}
        """
    else:
        return f"""
Your final Cards: {list(user_player.cards)}, and its score is {user_player.total_user_cards}
Computer's final cards: {list(computer_player.cards)} and its score is {computer_player.total_user_cards}
        """
        
def return_status_of_players(user_player, computer_player):
    
    display_cards_and_scores(user_player, computer_player, show_computer_cards=True)
       
    if user_player.lost_or_not_yet() and computer_player.lost_or_not_yet():
        return "Draw"
    if not user_player.lost_or_not_yet() and not computer_player.lost_or_not_yet():
        if user_player.total_user_cards == computer_player.total_user_cards:
            return "Draw"
        if user_player.total_user_cards > computer_player.total_user_cards:
            return "User Wins!\nComputer Lost"
        else:
            return "User Lost\nComputer Wins!"
    if user_player.is_a_blackjack() and computer_player.is_a_blackjack():
        return "Draw"
    if user_player.lost_or_not_yet() and computer_player.total_user_cards <= 21:
        return "User Lost\nComputer Wins!"
    if user_player.total_user_cards <= 21 and computer_player.lost_or_not_yet():
        return "User Wins!\nComputer Lost"
        

def computer_turn(user_player, computer_player):
    
    print(display_cards_and_scores(user_player, computer_player, show_computer_cards=True))
    
    status_of_players = return_status_of_players(user_player, computer_player)
    
    if status_of_players == "User Wins!\nComputer Lost":
        count = random.randint(0, 5)
        user_player.calculate_and_return_total_of_cards()
        for i in range(count):
            computer_player.cards.append(computer_player.get_new_card())
            computer_player.calculate_and_return_total_of_cards()
            print("Waiting for Computer's turn...")
            time.sleep(3)
            print(display_cards_and_scores(user_player, computer_player, show_computer_cards=True))
            
            
            if computer_player.is_a_blackjack():
                print("Computer has The BlackJack!")
                break
            if computer_player.total_user_cards > 21:
                print("Computer is Busted!")
                break
            
            status_of_players = return_status_of_players(user_player, computer_player)
            if status_of_players == "User Lost\nComputer Wins!":
                break
                
        
    return user_player, computer_player
    
    
    
def play_blackjack():
    os.system('cls')
    
    
    user_player = BlackJackUser()
    computer_player = BlackJackUser()
    game_off = False
    print(display_cards_and_scores(user_player, computer_player))

    def game_continue(user_player, computer_player, game_off = False):
            
        
        cont = input("Type 'y' to get another card, type 'n' to pass\n")
        
        if cont.capitalize() == 'N':
            user_player, computer_player = computer_turn(user_player, computer_player)
            game_off = True
            return user_player, computer_player, game_off
                
        else:
            user_player.cards.append(user_player.get_new_card())
            print(display_cards_and_scores(user_player, computer_player))
            user_player.calculate_and_return_total_of_cards()
            computer_player.calculate_and_return_total_of_cards()
                
            if user_player.is_a_blackjack():
                print("User has The BlackJack!")
            elif user_player.lost_or_not_yet():
                print("User is Busted!")
                
            if user_player.is_a_blackjack() or user_player.lost_or_not_yet():
                user_player, computer_player = computer_turn(user_player, computer_player)
                game_off = True

            return user_player, computer_player, game_off
        
    while not game_off:
        user_player, computer_player, game_off = game_continue(user_player, computer_player, game_off)
    
    print(return_status_of_players(user_player, computer_player))
                
    
        
play_blackjack()