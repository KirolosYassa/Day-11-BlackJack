import random
import os

CARDS = {"A": 10,
         "2": 2,
         "3": 3,
         "4": 4,
         "5": 5,
         "6": 6,
         "7": 7,
         "8": 8,
         "9": 9,
         "10": 10,
         "Q": 10,
         "K": 10,
         "J": 10,
    }

class BlackjackUser:
    
    def __init__(self):
        self.cards = [random.choice(list(CARDS.items())) for card in range(2)]
        self.total_user_cards = 0
        for card, value in self.cards:
            self.total_user_cards += value
    
    def calculate_and_return_total_of_cards(self):
        self.total_user_cards = 0
        for card, value in self.cards:
            self.total_user_cards += value
            
        if self.total_user_cards > 21: 
            for card, value in self.cards:
                if card == "A":
                    self.total_user_cards += 1

        return self.total_user_cards
    
    def get_new_card(self):
        new_card = random.choice(list(CARDS.items()))
        self.calculate_and_return_total_of_cards()
        return new_card
    
    def lost_or_not_yet(self):
        if self.calculate_and_return_total_of_cards() > 21:
            return True
        return False
    
    def is_a_blackjack(self):
        if self.calculate_and_return_total_of_cards() == 21:
            return True
        return False
        
    def get_only_first_card(self):
        # return list(self.cards.keys())[0]
        self.calculate_and_return_total_of_cards()
        return next(iter(self.cards))
    
        
    def get_total_cards_with_first_element_only(self):
        self.calculate_and_return_total_of_cards()
        return list(self.cards)[0]
        # return next(iter(self.cards))
    
    