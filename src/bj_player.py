from cards import Card
from cards import Deck


class BJ_Player:
    def __init__(self, name ,bet, id, dealer):
        self._name = name
        self._bet = int(bet)
        self._hand = []
        self._points = 0
        self._id = id
        self._over = False
        self._dealer = dealer
        self._earning = 0
        self._multiplier = 'Normal'
        print(f'Player {self._name} created')
        if dealer:
            print(f'{self._name} is the dealer')
        else:
            print(f'{self._name} is betting {self._bet}')

    @property
    def points(self):
        return self._points
    @points.setter
    def points(self, value):
        self._points = value
    @property
    def name(self):
        return self._name
    @property
    def over(self):
        return self._over
    @over.setter
    def over(self, value):
        self._over = value
    @property
    def hand(self):
        return self._hand
    @property
    def dealer(self):
        return self._dealer
    @property
    def bet(self):
        return self._bet
    @property
    def earning(self):
        return self._earning
    @earning.setter
    def earning(self, value):
        self._earning = value
    @property
    def multiplier(self):
        return self._multiplier
    @multiplier.setter
    def multiplier(self, value):
        self._multiplier = value


    def draw_card(self, deck):
        card = deck.draw_card()
        self._hand.append(card)
        self._points = 0
        for c in self._hand:
            c.ace_value(len(self._hand))
            self._points += c.bj_value
        if self._points > 21:
            recount = 0
            for c in self._hand:
                if c.value == 'Ace':
                    c.bj_value = 1
                recount += c.bj_value
            self._points = recount


    def __repr__(self):
        return f'{self._name} has {self._points} points. Cards:{self._hand}'





    
    