<script lang='ts'>
    import * as db from "$lib/backend/sample/test";
  
    let courses: any;
  
    // Define an async function and call it in onMount
    const fetchData = async () => {
      courses = await db.all_courses();
      console.log('Component courses:', courses);
    };
  
    import { onMount } from 'svelte';
    onMount(() => {
      fetchData();
    });
  </script>
  
  {#if courses}
    <ul>
      {#each courses.courses as course}
        <li>{course.info.name}</li>
        <li>{course.info.credits}</li>
        <li>{course.info.class_notes}</li>
      {/each}
    </ul>
  {:else}
    <p>Loading courses...</p>
  {/if}
  