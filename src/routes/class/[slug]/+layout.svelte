<script lang='ts'>
   import type { LayoutData } from './$types'
	export let data: LayoutData;
</script>

<main>
	<!-- +page.svelte is rendered in this <slot> -->
	<slot />
</main>

<h1>&lt layout starts here &gt</h1>

<aside>
	<h2>More posts:</h2>
	<ul>
		{#each data.posts as post}
			<li>
				<a href="/class/{post.slug}">
					{post.title}
				</a>
			</li>
		{/each}
	</ul>
</aside>