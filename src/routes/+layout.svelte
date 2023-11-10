<script lang="ts">
  import "../app.postcss";
  import Header from "./Header.svelte";
</script>


<div id="container">
  <div id="header">
    <Header />
  </div>

  <div id="main-section">
		<main>
			<slot />
			<!-- <Footer /> -->
		</main>
	</div>

</div>
