
<script>
    import { AppBar, AppShell } from '@skeletonlabs/skeleton';
	import { Avatar } from '@skeletonlabs/skeleton';
	import {onMount} from 'svelte';




	let currentMessage = '';

	let messagesFeed=[
		{
			id: 0,
			host: true,
			avatar: 48,
			name: 'Jobby',
			timestamp: 'Yesterday @ 2:30pm',
			message: 'ANYA FTW!!!!',
			color: 'variant-soft-primary'
		},
		{
		id: 1,
		host: false,
		avatar: 14,
		name: 'Maccy',
		timestamp: 'Yesterday @ 2:45pm',
		message: '.....',
		color: 'variant-soft-primary'
		},
		{
		id: 2,
		host: false,
		avatar: 23,
		name: 'anyafan',
		timestamp: 'Yesterday @ 2:50pm',
		message: 'ANYA FTW!!!!',
		color: 'variant-soft-primary'
		},
	];

	const sendChat = () =>{
		// console.log(currentMessage);
		// console.log(messagesFeed);
		messagesFeed = [...messagesFeed, {
			id: messagesFeed.length,
			host: false,
			avatar: 23,
			name: 'anyafan',
			timestamp: 'Yesterday @ 2:50pm',
			message: currentMessage,
			color: 'variant-soft-primary'
		}];
		currentMessage = '';
		// console.log(messagesFeed);
	}
</script>



<AppShell>
    <!-- (header) -->
	<!-- (sidebarLeft) -->
	<!-- (sidebarRight) -->
	<!-- (pageHeader) -->
	<!-- Router Slot -->
	<slot />
	<!-- ---- / ---- -->
	<svelte:fragment slot="pageFooter">
	<div class="h-full grid grid-rows-[1fr_200px] gap-1 ">
		<div class="bg-surface-500/30 p-4 overflow-y-auto">
			
			<section class="w-full max-h-[200px] p-4 overflow-y-auto space-y-4">
				{#each messagesFeed as bubble, i}
					{#if bubble.host === true}
						<!-- Host Message Bubble -->
						<!-- <pre>host: {JSON.stringify(bubble, null, 2)}</pre> -->
						
						<div class="grid grid-cols-[auto_1fr] gap-2">
							<Avatar initials="{bubble.name}" width="w-12" />
							<div class="card p-4 variant-soft rounded-tl-none space-y-2">
								<header class="flex justify-between items-center">
									<p class="font-bold">{bubble.name}</p>
									<small class="opacity-50">{bubble.timestamp}</small>
								</header>
								<p>{bubble.message}</p>
							</div>
						</div>
					
					{:else}
						<!-- Guest Message Bubble -->
						<!-- <pre>guest: {JSON.stringify(bubble, null, 2)}</pre> -->

						
						<div class="grid grid-cols-[1fr_auto] gap-2">
							<div class="card p-4 rounded-tr-none space-y-2 {bubble.color}">
								<header class="flex justify-between items-center">
									<p class="font-bold">{bubble.name}</p>
									<small class="opacity-50">{bubble.timestamp}</small>
								</header>
								<p>{bubble.message}</p>
							</div>
							<Avatar initials="{bubble.name}" width="w-12" />
						</div>
					
					{/if}
				{/each}
			</section>
					
			
		</div>
		<div class="bg-surface-500/30 p-1 inline-block">
			<!-- <div class="flex justify-between items-center">
				<input type="text" class="input input-ghost w-full" placeholder="Type a message..." />
				<button class="btn btn-sm btn variant-filled-primary">Send</button>
			</div> -->
			
			<div class="input-group input-group-divider grid-cols-[auto_1fr_auto] rounded-container-token">
				<button class="input-group-shim">+</button>
				<textarea
					bind:value={currentMessage}
					class="bg-transparent border-0 ring-0"
					name="prompt"
					id="prompt"
					placeholder="Write a message..."
					rows="1"
				/>
				<button class="variant-filled-secondary" on:click={sendChat}>Send</button>
			</div>
					
		</div>

	</div>
	</svelte:fragment>
	<!-- (footer) -->
</AppShell>


<style>
	section{
		scroll-behavior: smooth;
		border-radius: 10px;
	}
</style>