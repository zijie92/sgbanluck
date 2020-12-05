from cards import Card
from cards import Deck
from bj_player import BJ_Player
from bj_game import BJ_game

def main():
    num_players =  input('Number of Players: ')
    #num_players = 7
    dealer = False
    players = []
    for i in range(int(num_players)):
        name = input(f'Name of player {i+1} (First player will be the dealer): ')
        if not dealer:
            dealer = True
            # Dealer is first guy        
            players.append(BJ_Player('(Dealer) ' + name,0, i,True))
        else:
            #bet = input('How much to bet? ')
            bet = 200
            players.append(BJ_Player(name, bet,i, False))

    game = BJ_game(players)
    game.initiate_game()
    game.start_game()
    

# Here's our payoff idiom!
if __name__ == '__main__':
    main()