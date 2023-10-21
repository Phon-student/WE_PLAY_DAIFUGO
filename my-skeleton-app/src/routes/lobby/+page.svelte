<script>
    import axios from 'axios';
    let playerName = '';
    let card = '';
    let gameInfo = null;
    let scores = null;

    const startGame = () => {
        axios.post('http://localhost:8000/start_game', {
            player1: "foo4", 
            player2: "foo3", 
            player3: "foo2", 
            player4: "foo"
        })
        .then(function (response) {
            console.log(response);
            gameInfo = response.data;
        })
        .catch(function (error) {
            console.log(error);
        });

    }
</script>

<div id="response-container">
    <!-- This is where the response will be displayed -->
</div>

<button class="btn btn-primary variant-filled-secondary" on:click={startGame}>Start Game</button>
<input type="text" bind:value={playerName} placeholder="Player Name">
<input type="text" bind:value={card} placeholder="Card (e.g., [3, 'club'])">
<button class="btn btn-primary variant-filled-secondary" >Play Card</button>
<button class="btn btn-primary variant-filled-secondary" >Get Scores</button>

<style>
    .btn {
        margin: 0.5rem;
    }
</style>
