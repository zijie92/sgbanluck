
import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        if value == 'Ace':
            self.bj_value = 11
        elif (value == 'King' or value ==  'Queen' or value == 'Jack'):
            self.bj_value = 10
        else:
            self.bj_value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'

    def ace_value(self, num_cards):
        if self.value == 'Ace':
            if num_cards == 2:
                self.bj_value = 11
            if num_cards > 2:
                self.bj_value = 10

class Deck: 
    def __init__(self):
        self.cards = []

    def construct_new_deck(self):
        for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            for value in ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']:
                self.cards.append(Card(value,suit))
        random.shuffle(self.cards)

    def __repr__(self):
        return ', '.join(map(str,self.cards))


    # for bj
    def draw_card(self):
        return self.cards.pop()   
