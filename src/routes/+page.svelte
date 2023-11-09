<script lang='ts'>
    import { all_courses_names } from "$lib/backend/sample/test";
  
    let courses: any;
  
    // Define an async function and call it in onMount
    const fetchData = async () => {
      courses = await all_courses_names();
      console.log('Component courses:', courses);
    };
  
    import { onMount } from 'svelte';
    onMount(() => {
      fetchData();
    });
  </script>
  
  {#if courses}
    <ul>
      {#each courses.courses as course (course.name)}
        <li>{course.name}</li>
      {/each}
    </ul>
  {:else}
    <p>Loading courses...</p>
  {/if}
  