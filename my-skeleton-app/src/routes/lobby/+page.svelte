<script>
    import { post as startGameApi } from '$routes/api.js';
</script>


<button class="btn btn-sm btn variant-filled-primary mr-4" on:click={startGameApi}>Start Game</button>

async function startGame(){
    try {
        const res = await fetch('/api/start-game', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                roomID: roomID,
                userID: userID
            })
        });
        const data = await res.json();
        console.log(data);
    }catch(err){
        console.log(err);
    };

};
