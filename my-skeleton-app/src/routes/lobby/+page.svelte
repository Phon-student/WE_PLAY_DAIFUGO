<script>
    import axios from 'axios';
    import { onMount } from 'svelte';

    let gameInfo = null;
    let scores = null;
    let playerName = null;
    let card = null;
    
    const startGame = async () => {
        try {
            const response = await axios.get("/start-game");
            gameInfo = response.data.game_info;
            // Update the UI to display gameInfo
            responseContainer.innerText = "Game started!"; // Update the response container
        } catch (error) {
            console.error("Error starting the game", error);
        }
    };

    const playCard = async (playerName, card) => {
        try {
            const response = await axios.get("/play-card", { player_name: playerName, card: card });
            gameInfo = response.data.game_info;
            // Update the UI to display gameInfo
        } catch (error) {
            console.error("Error playing a card", error);
        }
    };

    const getScores = async () => {
        try {
            const response = await axios.get("/get-scores");
            scores = response.data.scores;
            // Update the UI to display scores
        } catch (error) {
            console.error("Error getting scores", error);
        }
    };
</script>

<div id="response-container">
    <!-- This is where the response will be displayed -->
</div>

<button class="btn btn-primary variant-filled-secondary" on:click={startGame}>Start Game</button>
<input type="text" bind:value={playerName} placeholder="Player Name">
<input type="text" bind:value={card} placeholder="Card (e.g., [3, 'club'])">
<button class="btn btn-primary variant-filled-secondary" on:click={() => playCard(playerName, card)}>Play Card</button>
<button class="btn btn-primary variant-filled-secondary" on:click={getScores}>Get Scores</button>

<style>
    .btn {
        margin: 0.5rem;
    }
</style>
