<script lang="ts">
  import { get_current_user } from "$lib/backend/db_get";
  import { supabase } from "$lib/backend/supabaseClient";
  import { Button } from "$lib/components/ui/button";
  import { onMount, } from "svelte";

  let show_logout: boolean = true;

$:  get_logged_in_status = async () => {
// data = await get_current_user()

  // if (data === null) {
  //   console.log("user null");
  //   show_logout = false;
  // } else{
// 	show_logout = true;
	// }
  };

  onMount(async () => {
    // Start the continuous update when the component is mounted
	
	// const intervalId = setInterval(get_logged_in_status, 1000); // Run every second

    // // Cleanup on component destruction
    // onDestroy(() => {
    //   clearInterval(intervalId);
    // });
  });

</script>

<header class="flex p-3 h-auto  ">
  <nav class=" justify-start items-start">
    <a href="/">
      <!-- change logo dark/light mode -->
      <h1 class="font-bold text-5xl pt-5 pl-9 group">
        <span class="underline decoration-yellow-300 decoration-8 hover:decoration-yellow-500">
          SlugPlanner
        </span>
      </h1>
    </a>
  </nav>

  <nav class=" flex w-full">
    <!-- left section -->

    <!-- middle section -->
    <ul
      class="flex justify-evenly items-center font-medium space-x-7 py-10 min-w-[25rem] w-full"
    >
      <li>
        <a
          class=" font-bold text-2xl underline decoration-blue-300 decoration-4 hover:decoration-blue-500"
          href="/class">All Classes</a
        >
      </li>

      <!-- <li>
        <a
          class=" font-bold text-2xl underline decoration-green-300 decoration-4"
          href="/fiddling_dingaling">fiddling_dingaling</a
        >
      </li> -->
      <li>
        <a
          class=" font-bold text-2xl underline decoration-green-300 decoration-4 hover:decoration-green-500"
          href="/select_prereqs">Change Prerequisites</a
        >
      </li>
      {#if show_logout}
        <li>
          <a
            class=" font-bold text-2xl underline decoration-red-300 decoration-4 hover:decoration-red-500"
            href="/logout">Logout</a
          >
        </li>
      {/if}

      <!-- <li class='flex items-center'>
				<a href="/contact">Contact</a>
				<CaretRight class="h-[1.5rem] w-[1.5rem]"/>
			</li> -->
    </ul>

    <!-- right section -->
    <div
      id="right"
      class="rounded-md w-52 pl-2 flex justify-between items-center"
    />
  </nav>
</header>
