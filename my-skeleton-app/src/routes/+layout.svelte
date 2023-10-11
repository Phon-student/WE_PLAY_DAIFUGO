<script lang="ts">
	import '../app.postcss';
	import {page} from '$app/stores';
	//input
	let currentMessage = '';

	//output
	let messages = [];

	// Skeleton UI
	import { AppBar, AppShell, Avatar, Drawer, getDrawerStore } from '@skeletonlabs/skeleton';
	import Navigation from '$lib/components/Navigation.svelte';
	import {LightSwitch, type DrawerSettings, type DrawerStore} from '@skeletonlabs/skeleton';
	import { initializeStores } from '@skeletonlabs/skeleton';
	import path from 'path';
	initializeStores();

	const drawerStore = getDrawerStore();

	function drawerOpen() {
		drawerStore.open();
	}



	// Chat UI
</script>

<Drawer>
	<Navigation />
</Drawer>

<AppShell regionPage="relative" slotPageHeader="sticky top-0 z-10" slotSidebarLeft="w-0 md:w-52 bg-surface-500/10">
	<svelte:fragment slot="header">
		<AppBar>
			<svelte:fragment slot="lead">
				<button class="md:hidden btn btn-sm mr-4" on:click={drawerOpen}>
					<span>
						<svg viewBox="0 0 100 80" class="fill-token w-4 h-4">
							<rect width="100" height="20"/>
							<rect y="30" width="100" height="20"/>
							<rect y="60" width="100" height="20"/>
						</svg>
					</span>
				</button>

				<strong class="text-xl uppercase font-bold">daifugo</strong>
			</svelte:fragment>
			<svelte:fragment slot="trail">
				<a class="btn btn-sm btn variant-soft-secondary mr-4"
					href="https://github.com/Phon-student/WE_PLAY_DAIFUGO"
					target="_blank">
					Github
				</a>
				<Avatar
					initials="SS" width="w-12 " background="bg-primary-500"
					border="border-4 border-surface-300-600-token hover:!border-primary-500"
					cursor="cursor-pointer" 
				/>
				<LightSwitch />
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<svelte:fragment slot="sidebarLeft">
		<Navigation />
	</svelte:fragment>
	<!-- (sidebarRight) -->
	<!-- Router Slot -->
	<div class="container p-10 mx-auto">

		<slot />
	</div>
	<!-- ---- / ---- -->
	<!-- (pageFooter) -->
	<svelte:fragment slot="pageFooter">
		{#if $page.path === '/lobby'}
			<p>{$page.url}</p>
		{/if}
		<label class="label flex items-center">
			<input class="input flex-1 mr-2" type="text" placeholder="Enter your text here..." />
			<button class="btn btn-sm btn variant-filled-primary mr-4">Send</button>
		</label>
	</svelte:fragment>
	<!-- (footer) -->
</AppShell>