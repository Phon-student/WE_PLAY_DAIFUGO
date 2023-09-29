<script>
    import { onMount } from 'svelte';
    
    export let tableArr = [
        { RoomName: "Jobby", RoomID: "999", Password: "None", Players: "1/4" },
        { RoomName: "Cherry", RoomID: "555", Password: "123", Players: "2/4" },
        { RoomName: "Pluem", RoomID: "420", Password: "None", Players: "4/4" },
    ];

    let tableState = true;

    function joinRoom() {
        tableState = false;
    }



</script>

{#if tableState}
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
            {#each tableArr as row, i}
            <tr>
                <td>{row.RoomName}</td>
                <td>{row.RoomID}</td>
                <td>{#if row.Password !== "None"}
                        <h1>Locked</h1>
                    {:else}
                        {row.Password}
                {/if}</td>
                <td>{row.Players}</td>
                <td>
                    {#if row.Players === "4/4"}
                        <button class="btn btn-sm btn variant-soft-primary mr-4" disabled>Full</button>
                    {:else if row.Password !== "None"}
                        <button class="btn btn-sm btn variant-filled-primary mr-4">Password Required</button>
                    {:else}
                        <button class="btn btn-sm btn variant-filled-primary mr-4" on:click={joinRoom}>Join</button>
                    {/if}
                </td>
            </tr>
            {/each}
        </tbody>
    </table>
</div>
{/if}
