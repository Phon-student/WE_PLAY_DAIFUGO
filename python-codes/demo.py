import itertools
import random
from time import time, sleep

heart = "\u2665"
spade = "\u2660"
diamond = "\u2666"
club = "\u2663"

deck = tuple(list(itertools.product(range(3, 11), [club, diamond, heart, spade])) + list(itertools.product(["J", "Q", "K", "A"], [club, diamond, heart, spade])) + list(itertools.product([2], [club, diamond, heart, spade])))

middle_card = None

# print(deck)

class Player:
    def __init__(self, player_name):
        self.hand = []
        self.player_name = player_name
        self.score = 0
        

class Game:
    def __init__(self):
        self.middle_card = None
        self.deck = None
        self.direction = None
        self.finished_players = {1: {1: None,
                                     2: None,
                                     3: None,
                                     4: None},
                                 2: {1: None,
                                     2: None,
                                     3: None,
                                     4: None}}

    def players(self, player1, player2, player3, player4):
        self.player_names = [Player(player1), Player(player2), Player(player3), Player(player4)]

    def scoring(self, round):
        self.finished_players[round][1].score += 2*round
        self.finished_players[round][2].score += 1*round
        self.finished_players[round][3].score -= 1*round
        self.finished_players[round][4].score -= 2*round
    
    def run(self, round):
        self.players = self.player_names.copy()
        self.nextposition = 1
        self.playerfinish = False
        self.active_players = [0, 1, 2, 3]
        self.deal_cards()

        if round == 1:
            self.player_turn(self.find_starter(), 'cw')

        
    def deal_cards(self):
        self.deck = list(deck).copy()
        # random.shuffle(self.deck)
        for i in range(4):
            for j in range(13):
                self.players[i].hand.append(self.deck.pop())
            self.players[i].hand = sorted(self.players[i].hand, key=deck.index)       
    
    def find_starter(self):
        for i in range(4):
            if self.players[i].hand[0] == (3, club):
                return i
    
    def throw(self, message):
        print("\033[F\033[K", end="")
        print('---', message, '---')
        sleep(1)
        print("\033[F\033[K", end="")
    
    def player_turn(self, player, direction):     
        current_player = self.players[self.active_players[player]]
        
# PRINT INFOS
        print(f'-----------------------------------------------------\n')
        print(f"It is {current_player.player_name}'s turn", self.active_players, [self.players[i].player_name for i in range(len(self.players))])
        # print(f"It is player {self.active_players[player]}'s turn", self.active_players, [self.players[i].player_name for i in range(len(self.players))])
        print("The middle card is: ", self.middle_card)
        # for i in range(len(self.players)):
        #     print(f"Player {i}'s hand is: ", self.players[i].hand)
        print("Your hand is: ", current_player.hand)
        
        print(' '*16, end='')       
        for n, i in enumerate(current_player.hand):
            if deck.index(i) < 28 or deck.index(i) > 47:
                print(f"   {n}       "[:10], end='')
            elif deck.index(i) < 32:
                print(f"   {n}        "[:11], end='')
            elif deck.index(i) < 48:
                print(f"    {n}        "[:12], end='')
        print('\n')
            
# INPUT CHOICES
        while 1:    
            choice = input("What card would you like to play?: ")
            if choice == 'pass':
                if not self.playerfinish:
                    self.active_players.pop(player)
                    player -= 1
                break 
            try:
                choice = sorted([int(i) for i in choice.split(' ')])
                   
# PLAYED CARDS HANDLER
                if len(choice) == 1:
                    if self.middle_card is not None:
                        if deck.index(current_player.hand[choice[0]]) < deck.index(self.middle_card[0]):
                            self.throw("You must play a card higher than the middle card")
                            continue
                        elif len(self.middle_card) != 1:
                            self.throw("You cannot play a single card now")
                            continue
                
                elif len(choice) == 2:
                    if current_player.hand[choice[0]][0] != current_player.hand[choice[1]][0]:
                            self.throw("You must play two cards of the same value")
                            continue
                    if self.middle_card is not None:             
                        if len(self.middle_card) != 2:
                            self.throw("You cannot play a pair now")
                            continue
                        elif deck.index(current_player.hand[choice[1]]) < deck.index(self.middle_card[1]):
                            self.throw("You must play a pair higher than the middle card")
                            continue
                        
                elif len(choice) == 3:              
                    if current_player.hand[choice[0]][0] != current_player.hand[choice[1]][0] or current_player.hand[choice[0]][0] != current_player.hand[choice[2]][0]:
                        self.throw("You must play three cards of the same value")
                        continue
                    elif self.middle_card is not None:             
                        if len(self.middle_card) == 1:
                            pass
                        elif len(self.middle_card) != 3:
                            self.throw("You cannot play a triple now")
                            continue
                        elif deck.index(current_player.hand[choice[2]]) < deck.index(self.middle_card[2]):
                            self.throw("You must play a triple higher than the middle card")
                            continue

                elif len(choice) == 4:
                    if current_player.hand[choice[0]][0] != current_player.hand[choice[1]][0] or current_player.hand[choice[0]][0] != current_player.hand[choice[2]][0] or current_player.hand[choice[0]][0] != current_player.hand[choice[3]][0]:
                        self.throw("You must play four cards of the same value")
                        continue
                    elif self.middle_card is not None:                   
                        if len(self.middle_card) == 2:
                            pass
                        elif len(self.middle_card) != 4:
                            self.throw("You cannot play a four of a kind now")
                            continue
                        elif deck.index(current_player.hand[choice[3]]) < deck.index(self.middle_card[3]):
                            self.throw("You must play a four of a kind higher than the middle card")
                            continue
                        
                self.middle_card = [current_player.hand.pop(choice[0]) for _ in range(len(choice))]
                break  
            
            except:
                self.throw("Invalid input")
                continue

        if self.playerfinish:
            self.playerfinish = False
        
# FINISHED PLAYER HANDLER
        if len(current_player.hand) < 10:
            self.finished_players[self.nextposition] = self.players.pop(self.active_players[player])
            if len(self.players) == 1:
                self.finished_players[self.nextposition + 1] = self.players[0]
                self.throw("Game ended")
                return
            player -= 1
            self.active_players = list(range(len(self.players)))
            self.nextposition += 1
            self.playerfinish = True
            # self.active_players.pop(player)

# ALL PLAYERS PASSED HANDLER
        if len(self.active_players) == 1:
            self.throw("All other players have passed")
            self.middle_card = None
            player = self.active_players[0]
            self.active_players = list(range(len(self.players)))
            for _ in range(7):
                print("\033[F\033[K", end="")
            return self.player_turn(player, 'cw')            
        
# CLEAR LINES
        for _ in range(8):
            print("\033[F\033[K", end="")
        
# NEXT PLAYER
        if direction == 'cw':
            if player < len(self.active_players) - 1:
                return self.player_turn((player + 1), direction)
            else:
                player = 0
                return self.player_turn(0, direction)
        elif direction == 'ccw':
            if player > 0:
                return self.player_turn((player - 1), direction)
            else:
                player = len(self.active_players) - 1
                return self.player_turn(len(self.active_players-1)), direction
    
        

game1 = Game()
game1.players('player0', 'player1', 'player2', 'player3')
game1.round1()




# def setup(deck):
#     shuffled_deck = deck.copy()
#     random.shuffle(shuffled_deck)
#     player_hands = [[], [], [], []]
#     for i in range(4):
#         for j in range(13):
#             player_hands[i].append(shuffled_deck.pop())
    
#     return {'player1': sorted(player_hands[0], key=deck.index), 
#             'player2': sorted(player_hands[1], key=deck.index), 
#             'player3': sorted(player_hands[2], key=deck.index), 
#             'player4': sorted(player_hands[3], key=deck.index)}

# def find_starter(decks_dict):
#     for i in decks_dict:
#         if decks_dict[i][0] == (3, '♣'):
#             return i
        
# def player_turn(player, middle_card, direction):
#     print('\n')
#     print(f"It is {player}'s turn")
#     print("The middle card is: ", middle_card)
#     print("Your hand is: ", player_hands[player])
#     choice = int(input("What card would you like to play?: "))
#     middle_card = player_hands[player].pop(choice)
#     if len(player_hands[player]) == 0:
#         return
#     else:
#         for _ in range(6):
#             print("\033[F\033[K", end="")

#         player_turn(next_player(player, direction), middle_card, direction)

    
# def next_player(player, direction):
#     if direction == 'cw':
#         if player == 'player4':
#             return 'player1'
#         else:
#             return 'player' + str(int(player[6:]) + 1)
#     elif direction == 'ccw':
#         if player == 'player1':
#             return 'player4'
#         else:
#             return 'player' + str(int(player[6:]) - 1)
        
# player_hands = setup(deck)
# current_player = find_starter(player_hands)

# player_turn(current_player, None, 'cw')
