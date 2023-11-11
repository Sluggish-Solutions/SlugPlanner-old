<script lang="ts">
    import type { PageData } from './$types';
    
    export let data: PageData;


</script>

{#if data.status}
<h1>logout success</h1>
{:else}
<h1>something went wrong</h1>
{/if}
