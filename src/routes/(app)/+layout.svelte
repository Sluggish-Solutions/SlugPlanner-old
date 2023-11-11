<script lang="ts">
	import '../../app.postcss'
	import Header from '../Header.svelte'
</script>

<div id="container">
	<div id="header" class="h-[15vh] border-2 border-gray-300 ">
		<Header />
	</div>

	<div id="main-section" class="h-[85vh] ">
		<main>
			<slot />
			<!-- <Footer /> -->
		</main>
	</div>
</div>
