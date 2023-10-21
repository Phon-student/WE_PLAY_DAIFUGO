import itertools
import random
from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


heart = "\u2665"
spade = "\u2660"
diamond = "\u2666"
club = "\u2663"

deck = tuple(list(itertools.product(range(3, 11), [club, diamond, heart, spade])) + list(itertools.product(["J", "Q", "K", "A"], [club, diamond, heart, spade])) + list(itertools.product([2], [club, diamond, heart, spade])))

class Player:
    def __init__(self, player_name):
        self.hand = []
        self.player_name = player_name
        self.score = 0

class Game:
    def __init__(self):
        self.deck = None
        self.finish_position = {1: {1: None, 2: None, 3: None, 4: None}}

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

            # Your existing code for round 2

    def player_turn_loop(self, position, direction):
        while not self.playerfinish:
            self.player_turn(position)
            position = self.nextposition
            if direction == 'cw':
                self.nextposition = (self.nextposition + 1) % 4
            else:
                self.nextposition = (self.nextposition - 1) % 4

    def player_card_handling(self, position, card):
        self.players[position].hand.remove(card)
        self.middle_card = card
        self.active_players.remove(position)
        if len(self.active_players) == 1:
            self.playerfinish = True
            self.finish_position[self.round][self.active_players[0] + 1] = self.players[position]

    def get_valid_cards(self, position):
        valid_cards = []
        for card in self.players[position].hand:
            if card[1] == self.middle_card[1]:
                valid_cards.append(card)
        if len(valid_cards) == 0:
            valid_cards = self.players[position].hand.copy()
        return valid_cards

    def player_turn(self, position):
        valid_cards = self.get_valid_cards(position)
        card = self.players[position].hand[0]
        self.player_card_handling(position, card)
    
    
        # Add FastAPI routes to interact with the game

@app.get("/")
def read_root():
    return {"message": "Welcome to the card game API"}

@app.post("/start_game")
def start_game(player1: str, player2: str, player3: str, player4: str):
    game1 = Game()
    game1.players(player1, player2, player3, player4)
    game1.run()
    game1.scoring()
    return {"message": "Game started and scored"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
