<!-- YourParentComponent.svelte -->
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

  let quarter_data = {
    quarter1: {
      quarter_year: "Fall 2023",
      data: ["CSE 30", "MATH 21", "CLNI 1"]
    },
    quarter2: {
      quarter_year: "Winter 2024",
      data: ["CSE 12", "MATH 23A", "PHYS 5A", "PHYS 5L"]
    },
    quarter3: {
      quarter_year: "Spring 2024",
      data: ["CSE 30", "MATH 21", "CLNI 9"]
    },
    quarter4: {
      quarter_year: "Fall 2024",
      data: ["CSE 30", "MATH 21", "CLNI 9"]
    },
    quarter5: {
      quarter_year: "Winter 2025",
      data: ["CSE 30", "MATH 21", "CLNI 9"]
    },
    quarter6: {
      quarter_year: "Spring 2025",
      data: ["CSE 30", "MATH 21", "CLNI 9"]
    },
    quarter7: {
      quarter_year: "Fall 2025",
      data: ["CSE 30", "MATH 21", "CLNI 9"]
    },
    quarter8: {
      quarter_year: "Winter 2026",
      data: ["CSE 30", "MATH 21", "CLNI 9"]
    },
    quarter9: {
      quarter_year: "Spring 2026",
      data: ["CSE 30", "MATH 21", "CLNI 9"]
    },
    quarter10: {
      quarter_year: "Fall 2026",
      data: ["CSE 30", "MATH 21", "CLNI 9"]
    },
    quarter11: {
      quarter_year: "Winter 2027",
      data: ["CSE 30", "MATH 21", "CLNI 9"]
    },
    quarter12: {
      quarter_year: "Spring 2027",
      data: ["CSE 30", "MATH 21", "CLNI 9"]
    },
    
  }
</script>


<div class= "px-[14rem] py-2">
  <h1 class="text-center p-1 pt-6 font-bold underline decoration-slate-600 text-xl mb-2">Sample Schedule</h1>
  <div class=" p-9  border-2 rounded-2xl  border-gray">

  <div class="wrapper grid grid-cols-3 grid-rows-4 gap-2">
    <Quarter quarter_obj={quarter_data.quarter1} />
    <Quarter quarter_obj={quarter_data.quarter2}/>
    <Quarter quarter_obj={quarter_data.quarter3}/>
    <Quarter quarter_obj={quarter_data.quarter4}/>
    <Quarter quarter_obj={quarter_data.quarter5}/>
    <Quarter quarter_obj={quarter_data.quarter6}/>
    <Quarter quarter_obj={quarter_data.quarter7}/>
    <Quarter quarter_obj={quarter_data.quarter8}/>
    <Quarter quarter_obj={quarter_data.quarter9}/>
    <Quarter quarter_obj={quarter_data.quarter10}/>
    <Quarter quarter_obj={quarter_data.quarter11}/>
    <Quarter quarter_obj={quarter_data.quarter12}/>

  </div>
</div>
</div>