from fastapi import FastAPI, HTTPException, requests, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse
import random
from time import sleep
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

class StartGameRequest(BaseModel):
    player_names: list

# Simplified Game class may need more implementation
class Game:
    def __init__(self):
        self.players = []
        self.deck = []

    def start_game(self, player_names):
        self.players = [{"name": name, "hand": []} for name in player_names]
        self.deck = self.initialize_deck()
        self.deal_cards()

    def initialize_deck(self):
        suits = ["♠", "♡", "♢", "♣"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        deck = [{"value": value, "suit": suit} for suit in suits for value in values]
        random.shuffle(deck)
        return deck

    def deal_cards(self):
        for _ in range(13):
            for player in self.players:
                card = self.deck.pop()
                player["hand"].append(card)

    def play_card(self, player_name, card):
        for player in self.players:
            if player["name"] == player_name:
                if card in player["hand"]:
                    player["hand"].remove(card)
                    return True
        return False

    def get_scores(self):
        scores = {player["name"]: 0 for player in self.players}
        return scores

game = Game()

# Start a new game
@app.post("/start-game")
async def start_game(request: Request, player_names: list):
    game.start_game(player_names)
    return {"message": "Game started", "game_info": game.players}

# Play a card
@app.post("/play-card")
async def play_card(player_name: str, card: dict):
    if game.play_card(player_name, card):
        return {"message": f"{player_name} played a card", "game_info": game.players}
    else:
        raise HTTPException(status_code=400, detail="Invalid card or player not found")

# Get scores
@app.get("/get-scores")
async def get_scores():
    scores = game.get_scores()
    return {"scores": scores}

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
