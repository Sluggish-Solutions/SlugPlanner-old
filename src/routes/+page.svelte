<script lang='ts'>
    export let data;
    // console.log(data.courses.length)
  </script>

  <ul>
    {#each data.courses as course}
      <li>{course.name}</li>
    {/each}
  </ul>