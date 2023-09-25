<script>
    export let tableArr = [
        {name: "Jobby", id: "123", score: "100"},
        {name: "Cherry", id: "555", score: "70"},
    ];
     
</script>


<div class="table-container">
    <table class="table table-hover">
        <thead>
            <tr>
                <th>Players</th>
                <th>ID</th>
                <th>Score</th>
                <th>Rank</th>
            </tr>

        </thead>

        <tbody>
            {#each tableArr as row,i}
            <tr>
                <td>{row.name}</td>
                <td>{row.id}</td>
                <td>{row.score}</td>
                <td>{i+1}</td>
            </tr>
            {/each}

        </tbody>
    </table>
</div>