<!-- YourParentComponent.svelte -->
<script lang="ts">
  import { goto } from '$app/navigation';
  import Quarter from '$lib/components/Quarter.svelte';
  import { onMount } from 'svelte';

  export let data;

  onMount(() => {
    if (data.user === null) {
      goto("/login");
    }
  });
</script>

<style>
  /* Ensure the body and HTML have 100% height */
  html, body {
    height: 100%;
    margin: 0; /* Remove default margin */
    padding: 0; /* Remove default padding */
  }

  /* Ensure the entire container has 100% height */
  #app {
    height: 100%;
    display: flex;
    flex-direction: column;
  }

  /* Ensure the content area fills the remaining height */
  .content {
    flex-grow: 1;
  }

  /* Ensure the wrapper has 100% height */
  .wrapper {
    height: 100%;
  }
</style>
<div class= "px-[14rem]">
<div class="p-12 border border-cyan-400">
  <div class="wrapper grid grid-cols-3 grid-rows-4 gap-2">
    <Quarter quarter_year="lol" />
    <Quarter class1="AM 10"/>
    <Quarter />
    <Quarter />
    <Quarter />
    <Quarter />
    <Quarter />
    <Quarter />
    <Quarter />
    <Quarter />
    <Quarter />
  </div>
</div>
</div>