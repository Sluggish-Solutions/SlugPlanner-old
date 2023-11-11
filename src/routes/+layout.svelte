<script lang="ts">
  import "../app.postcss";
  import Header from "./Header.svelte";
</script>


<div id="container">
  
  <div id="root">
		<main>
			<slot />
			<!-- <Footer /> -->
		</main>
	</div>

</div>
