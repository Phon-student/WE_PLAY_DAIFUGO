
<script>
    import { AppBar, AppShell } from '@skeletonlabs/skeleton';

    import {Chat} from '$lib/components/Chat.svelte';
    
    
</script>


<AppShell>
    <!-- (header) -->
	<!-- (sidebarLeft) -->
	<!-- (sidebarRight) -->
	<!-- (pageHeader) -->
	<!-- Router Slot -->
	<slot />
	<!-- ---- / ---- -->
	<svelte:fragment slot="pageFooter">Page Footer</svelte:fragment>
	<!-- (footer) -->
</AppShell>