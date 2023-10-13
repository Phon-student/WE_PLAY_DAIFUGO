import itertools
import random
from time import sleep

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
        self.deck = None
        self.finish_position = {1: {1: None, 
                                    2: None,
                                    3: None,
                                    4: None},
                                2: {1: None,
                                    2: None,
                                    3: None,
                                    4: None}}

    def players(self, player1, player2, player3, player4):
        self.player_names = [Player(player1), Player(player2), Player(player3), Player(player4)]
    
    def deal_cards(self):
        self.deck = list(deck).copy()
        random.shuffle(self.deck)
        for i in range(4):
            self.players[i].hand = []
            for j in range(13):
                self.players[i].hand.append(self.deck.pop())
            self.players[i].hand = sorted(self.players[i].hand, key=deck.index)       
    
    def find_starter(self):
        for i in range(4):
            if self.players[i].hand[0] == (3, club):
                return i
    
    def scoring(self):
        for round in range(1, 3):
            self.finish_position[round][1].score += 2*round
            self.finish_position[round][2].score += 1*round
            self.finish_position[round][3].score -= 1*round
            self.finish_position[round][4].score -= 2*round

    def printscores(self):        
        print(f"-----------------------------------------------------\n")
        for i in self.player_names:
            print(f"{i.player_name}'s score is: {i.score}")
    
    def run(self):
        self.runround(1)
        self.runround(2)
    
    
    def runround(self, round):
        self.round = round
        self.middle_card = None
        self.players = self.player_names.copy()
        self.nextposition = 1
        self.playerfinish = False
        self.active_players = [0, 1, 2, 3]
        self.deal_cards()

        if round == 1:
            self.player_turn_loop(self.find_starter(), 'cw')
        else:
            direction = 'ccw'  
            print(f'-----------------------------------------------------\n')
            print(f"Hi, {self.finish_position[1][1].player_name}!")
            self.printhand(self.finish_position[1][1].hand)
                
            while True:   
                king_swap = input("Please select 2 cards to swap with slave: ")
                
                try:
                    king_swap = [int(i) for i in king_swap.split(' ')]
                    if len(king_swap) != 2:
                        raise Exception
                    self.finish_position[1][1].hand[king_swap[0]], self.finish_position[1][4].hand[-1], self.finish_position[1][1].hand[king_swap[1]], self.finish_position[1][4].hand[-2] = self.finish_position[1][4].hand[-1], self.finish_position[1][1].hand[king_swap[0]], self.finish_position[1][4].hand[-2], self.finish_position[1][1].hand[king_swap[1]]
                    break
                except:
                    print("\033[F\033[K", end="")
                    print("--- Invalid input ---", end="\r")
                    sleep(1)
            
            print("\033[F\033[K"*7, end="")
            
            print(f'-----------------------------------------------------\n')
            print(f"Hi, {self.finish_position[1][2].player_name}!")
            self.printhand(self.finish_position[1][2].hand)
                
            while True:
                try:    
                    queen_swap = int(input(f"{self.finish_position[1][2].player_name} please select 1 card to swap with vice-slave: "))
                    self.finish_position[1][2].hand[queen_swap], self.finish_position[1][3].hand[-1] = self.finish_position[1][3].hand[-1], self.finish_position[1][2].hand[queen_swap]
                    break
                except:
                    print("\033[F\033[K", end="")
                    print("--- Invalid input ---", end="\r")
                    sleep(1)
            
            print("\033[F\033[K"*7, end="")

            for i in range(4):
                self.players[i].hand = sorted(self.players[i].hand, key=deck.index)
            
            king_pos = self.players.index(self.finish_position[1][1])
            slave_pos = self.players.index(self.finish_position[1][4])

            if slave_pos - king_pos  in [1, -3]:
                direction = 'cw'

            self.player_turn_loop(self.player_names.index(self.finish_position[1][4]), direction)
    
    def printhand(self, hand):
        print("Your hand is: ", hand)
        print(' '*16, end='')       
        for n, i in enumerate(hand):
            if deck.index(i) < 28 or deck.index(i) > 47:
                print(f"   {n}       "[:10], end='')
            elif deck.index(i) < 32:
                print(f"   {n}        "[:11], end='')
            elif deck.index(i) < 48:
                print(f"    {n}        "[:12], end='')
        print('\n')
    
    def throw(self, message):
        print("\033[F\033[K", end="")
        print('---', message, '---')
        sleep(1)
        print("\033[F\033[K", end="")
    
    def player_turn_loop(self, player, direction):     
        while True:
            current_player = self.players[self.active_players[player]]
            
    # PRINT INFOS
            print(f'-----------------------------------------------------\n')
            print(f"It is {current_player.player_name}'s turn", self.active_players, [self.players[i].player_name for i in range(len(self.players))])
            # print(f"It is player {self.active_players[player]}'s turn", self.active_players, [self.players[i].player_name for i in range(len(self.players))])
            print("The middle card is: ", self.middle_card)
            # for i in range(len(self.players)):
            #     print(f"Player {i}'s hand is: ", self.players[i].hand)
            self.printhand(current_player.hand)
                        
    # INPUT CHOICES
            while True:    
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
            if len(current_player.hand) == 0:
                self.finish_position[self.round][self.nextposition] = self.players.pop(self.active_players[player])
                if self.nextposition == 1 and self.round == 2:
                    if current_player != self.finish_position[1][1]:
                        self.finish_position[2][4] = self.players.pop(self.players.index(self.finish_position[1][1]))

                if len(self.players) == 1:
                    self.finish_position[self.round][self.nextposition + 1] = self.players[0]
                    self.throw("Game ended")
                    print("\033[F\033[K"*7, end="")
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
                print("\033[F\033[K"*7, end="")
                # return self.player_turn(player, 'cw')      
                continue      
            
    # CLEAR LINES
            print("\033[F\033[K"*8, end="")
            
    # DETERMINING NEXT PLAYER
            if direction == 'cw':
                if player < len(self.active_players) - 1:
                    player += 1
                else:
                    player = 0
            elif direction == 'ccw':
                if player > 0:
                    player -= 1
                else:
                    player = len(self.active_players) - 1
                
            
def main():  
    game1 = Game()
    game1.players('player0', 'player1', 'player2', 'player3')
    game1.run()
    game1.scoring()

if __name__ == "__main__":
    main()