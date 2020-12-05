from cards import Card
from cards import Deck
from bj_player import BJ_Player

# todo: dealer should be able to open ppl before drawing another

multiplier = {
    'BlackJack': 2,
    'Double Aces': 3,
    'Run': 0,
    'Triple 7s': 7,
    '5 Dragon': 2,
    'Normal': 1
}



class BJ_game:
    def __init__(self, player_list):
        self.player_list = player_list
        self.deck = Deck()
        self.deck.construct_new_deck()
        # Move dealer to end
        player_list.append(player_list.pop(0))
        self.game_end = False

    def initiate_game(self):
        for i in range(2):
            for player in self.player_list:
                player.draw_card(self.deck)
        
        start_prompt = """
        #################################################################################
        #################################################################################
                                            Game Start 
        #################################################################################
        #################################################################################
        """

        print(start_prompt)
    
    def check_starting_hands(self, player):
        if len(player.hand) == 2:
            if player.points == 21:
                player.multiplier = 'BlackJack'
                player.over = True                
                if player.dealer:
                    print('Banker has BlackJack - game ends')
                else:
                    print(f'{player.name} has BlackJack! Congrats!')
            elif player.points == 15:
                player.multiplier = 'Run'
                player.over = True
                if player.dealer:
                    print('Banker runs with 15 - game ends')
                else:
                    print(f'{player.name} runs with 15...')
            elif player.hand[0].value == 'Ace' and player.hand[1].value == 'Ace':
                player.multiplier = 'Double Aces'
                player.over = True
                if player.dealer:
                    print('Banker has double Aces - game ends')
                else:
                    print(f'{player.name} has Double Aces! Congrats!')   

    def establish_winners(self):
        dealer = self.player_list[-1]
        # Dealer is winner
        # Double aces beats blackjack (takes precedence)
        if dealer.multiplier == 'Double Aces':
             for player in self.player_list[:-1]:
                if player.multiplier != dealer.multiplier:
                    player.earning = -multiplier[dealer.multiplier] * player.bet
                    dealer.earning += -player.earning         
        elif dealer.multiplier == 'BlackJack' or dealer.multiplier == '5 Dragon' or dealer.multiplier == 'Triple 7s':
            for player in self.player_list[:-1]:
                if player.multiplier != dealer.multiplier:
                    player.earning = -multiplier[dealer.multiplier] * player.bet
                    dealer.earning += -player.earning
        elif dealer.multiplier == 'Run':
            for player in self.player_list[:-1]:
                player.earning = 0
                dealer.earning = 0
        else:
            for player in self.player_list[:-1]:
                if player.multiplier == 'Double Aces':
                    player.earning = multiplier[player.multiplier] * player.bet
                    dealer.earning -= player.earning  
                elif player.multiplier == 'BlackJack' or player.multiplier == '5 Dragon' or player.multiplier == 'Triple 7s':
                    player.earning = multiplier[player.multiplier] * player.bet
                    dealer.earning -= player.earning    
                elif player.multiplier == 'Run':
                    player.earning = 0
                    dealer.earning += 0
                else:
                    if player.points > dealer.points:                      
                        player.earning = multiplier[player.multiplier] * player.bet
                        dealer.earning += -player.earning
                    elif player.points < dealer.points:
                        player.earning = -multiplier[player.multiplier] * player.bet
                        dealer.earning += -player.earning
                    else:
                        player.earning = 0
                        dealer.earning += 0 


    def round_results(self):
        self.establish_winners()
        result_prompt = """
        #################################################################################
        #################################################################################
                                            Round Result
        #################################################################################
        #################################################################################
        """
                
        for player in self.player_list:
            if player.points ==-1:
                res = 'Bust'
            else:
                res = player.points
            if not player.dealer:
                if player.earning > 0:
                    result = 'won'
                elif player.earning < 0:
                    result = 'lost'
                else:
                    result = 'drew'
                print(f'Player {player.name} has {result} against the dealer with a {res}, net profit/loss ========  {player.earning}')
            else:
                print(f"Dealer {player.name} has {res} Result: Net profit/loss =========== {player.earning}")
                if player.multiplier != 'Normal':
                    print(f"Dealer has a {player.multiplier}")

    def start_game(self):
        self.check_starting_hands(self.player_list[-1])
        if not self.player_list[-1].over:
            players_bust_mul = 0 
    # Auto-Run, Auto-BlackJack    
            for player in self.player_list:
                if not player.dealer:
                    print(f'Banker is showing: {self.player_list[-1].hand[-1]} ')
                print(f'Hi {player.name}, your turn. \n\n{player}')
                while not player.over:
                    # All players Bust
                    if players_bust_mul == len(self.player_list)-1 and player.dealer:
                        player.over = True                       
                    # player 15, 21
                    self.check_starting_hands(player)
                    if not player.over:
                        if player.points < 16:
                            choice = int(input('1. Hit\n'))                            
                        else:
                            choice = int(input('1. Hit \n2. Stand \n'))
                        if choice == 2:
                            player.over = True
                            print(f'{player.name} Stand with {player.points} points')
                        elif choice == 1:
                            player.draw_card(self.deck)
                            print(f"A has drawn {player.hand[-1]} \n{player}\n")
                            if len(player.hand) == 5 and player.points <= 21:
                                player.multiplier = '5 Dragon'
                            elif len(player.hand) == 3:
                                for c in player.hand:
                                    if c.value != 7:
                                        break
                                    player.multipler = 'Triple 7s'
                            if player.points > 21:
                                print('BUST\n')
                                player.over= True
                                player.points = -1
                                players_bust_mul += 1
                    else:
                        players_bust_mul += 1
                print('#################################################################################')
        else:
            for player in self.player_list[:-1]:
                self.check_starting_hands(player)

        self.round_results()


