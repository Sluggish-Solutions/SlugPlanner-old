<script lang="ts">
  import { goto } from '$app/navigation';
  import Quarter from '$lib/components/quarter.svelte';
  import { onMount } from 'svelte';

  export let data;

  onMount(() => {
    if (data.user === null) {
      goto("/login");
    }
  });
</script>


<div class="wrapper grid grid-cols-3 gap-4">
  <Quarter />
</div>