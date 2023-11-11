<!-- YourParentComponent.svelte -->
<script lang="ts">
  import { goto } from '$app/navigation';
  import Quarter from '$lib/components/quarter.svelte';
  import { onMount } from 'svelte';

  export let data;

  onMount(() => {
    console.log(data.user)
    if (data.user === null) {
      goto("/login");
    }
  });


  let quarter_data = {
    quarter1: {
      underline_col : "green",
      quarter_year: "Fall 2023",
      data: ["MATH 19A", "CSE 30", "CLNI 1"]
    },
    quarter2: {
      quarter_year: "Winter 2024",
      data: ["MATH 19B", "WRIT 1", "PHYS 5A", "PHYS 5L"]
    },
    quarter3: {
      quarter_year: "Spring 2024",
      data: ["MUSC 60", "AM 30", "CSE 12"]
    },
    quarter4: {
      quarter_year: "Fall 2024",
      data: ["AM 10", "PHYS 5C", "PHYS 5N", "CSE 16"]
    },
    quarter5: {
      quarter_year: "Winter 2025",
      data: ["CSE 13S", "CSE 40", "WRIT 2"]
    },
    quarter6: {
      quarter_year: "Spring 2025",
      data: ["CSE 101", "PHYS 5B", "PHYS 5M", "CSE120"]
    },
    quarter7: {
      quarter_year: "Fall 2025",
      data: ["ECE 101", "ECE 101L", "CSE 130", "CSE 3" ]
    },
    quarter8: {
      quarter_year: "Winter 2026",
      data: ["CSE 107", "CSE 100", "CSE 100L"]
    },
    quarter9: {
      quarter_year: "Spring 2026",
      data: ["CSE 121", "CSE 185E", "CSE 115A"]
    },
    quarter10: {
      quarter_year: "Fall 2026",
      data: ["CSE 115B", "ECE 103", "ECE 103L", "PHIL 9"]
    },
    quarter11: {
      quarter_year: "Winter 2027",
      data: ["CSE 115C", "CSE 130", "CSE 150"]
    },
    quarter12: {
      quarter_year: "Spring 2027",
      data: ["CSE 113", "HIS 2A", "OCEA 80A"]
    },
    
  }
</script>


<div class= "px-[14rem] py-2">
  <h1 class="text-center p-1 pt-6 font-bold underline decoration-slate-600 text-xl mb-2">Sample Schedule</h1>
  <div class=" p-9  border-2 rounded-2xl  border-grey">

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