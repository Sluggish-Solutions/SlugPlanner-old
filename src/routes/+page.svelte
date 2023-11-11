<script lang="ts">
  import { goto } from '$app/navigation';
  import { redirect } from '@sveltejs/kit';
 import { onMount } from 'svelte';

    export let data;

    console.log(data)
    onMount(() => {
        if(data.user === null){
        goto("/login")
    }
  });

</script>