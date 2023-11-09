<script lang='ts'>
  import type { PageData } from "./$types";


  export let data: PageData;

  let names = data.names
  $:console.log(data)

 </script>
  
  {#if names}
    <ul>
      {#each names.courses as course (course.name)}
        <li>{course.name}</li>
      {/each}
    </ul>
  {:else}
    <p>Loading courses...</p>
  {/if}
  