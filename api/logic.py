from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)


import itertools
import random
from time import sleep

heart = "\u2665"
spade = "\u2660"
diamond = "\u2666"
club = "\u2663"

deck = tuple(list(itertools.product(range(3, 11), [club, diamond, heart, spade])) + list(itertools.product(["J", "Q", "K", "A"], [club, diamond, heart, spade])) + list(itertools.product([2], [club, diamond, heart, spade])))

middle_card = None

class Player:
    def __init__(self, player_name):
        self.hand = []
        self.player_name = player_name
        self.score = 0

class Game:
    def __init__(self):
        self.deck = None
        self.finish_position = {
            1: {1: None, 2: None, 3: None, 4: None},
            2: {1: None, 2: None, 3: None, 4: None}
        }

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
            self.finish_position[round][1].score += 2 * round
            self.finish_position[round][2].score += 1 * round
            self.finish_position[round][3].score -= 1 * round
            self.finish_position[round][4].score -= 2 * round

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

            if slave_pos - king_pos in [1, -3]:
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

            # Rest of your player_turn_loop logic here

    # Rest of your Game class methods

# Implement the main FastAPI endpoints, e.g., start_game, play_card, get_scores, etc.


@app.post("/start-game")
async def start_game():
    # Create a new game instance, deal cards, and return relevant game information
    game = Game()
    game.players("Player1", "Player2", "Player3", "Player4")
    game.run()
    return {"message": "Game started", "game_info": ...}  # Replace ... with relevant game data

# Play a card
@app.post("/play-card")
async def play_card(player_name: str, card: tuple):
    # Implement logic to play a card for the specified player

    
    # Update game state and return relevant game information
    return {"message": f"{player_name} played a card", "game_info": ...}  # Replace ... with relevant game data

# Get scores
@app.get("/get-scores")
async def get_scores():
    # Return the current scores of the game
    return {"scores": ...}  # Replace ... with the actual score data

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Run the FastAPI app if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

    


