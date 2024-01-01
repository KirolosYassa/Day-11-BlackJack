import random
import os

class BlackjackUser:
    
    def __init__(self):
        self.cards = [self.get_new_card() for card in range(2)]
        self.total_user_cards = 0
        for card in self.cards:
            self.total_user_cards += card
    
    def calculate_and_return_total_of_cards(self):
        self.total_user_cards = 0
        for card in self.cards:
            self.total_user_cards += card
            
        if self.total_user_cards > 21: 
            for card in self.cards:
                if card == 10:
                    self.total_user_cards += 1

        return self.total_user_cards
    
    def get_new_card(self):
        return random.randint(1, 10)