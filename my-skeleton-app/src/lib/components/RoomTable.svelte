<script>
    export let tableArr = [
        {RoomName: "Jobby", RoomID: "999", Password: "None", Players: "1/4"},
        {RoomName: "Cherry", RoomID: "555", Password: "None", Players: "2/4"},
    ];
     
</script>


<div class="table-container">
    <table class="table table-hover">
        <thead>
            <tr>
                <th>Room name</th>
                <th>Room ID</th>
                <th>Password</th>
                <th>Players</th>
                <th></th>
            </tr>

        </thead>

        <tbody>
            {#each tableArr as row,i}
            <tr>
                <td>{row.RoomName}</td>
                <td>{row.RoomID}</td>
                <td>{row.Password}</td>
                <td>{row.Players}</td>
                <!-- button to the side -->
                <td><button class="btn btn-sm btn variant-filled-primary mr-4">Join</button></td>
            </tr>
            {/each}

        </tbody>
    </table>
</div>