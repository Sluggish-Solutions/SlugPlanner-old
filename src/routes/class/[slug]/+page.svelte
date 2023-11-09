<script lang='ts'>
	// /** @type {import('./$types').PageData} */
   import type { PageData } from './$types'
	export let data: PageData
	
	import { page } from '$app/stores';
	// we can access `data.posts` because it's returned from
	// the parent layout `load` function
	$: index = data.posts.findIndex(post => post.slug === $page.params.slug);
	$: next = data.posts[index + 1] || data.posts[index - 1];
</script>

<h1>{data.post.title}</h1>
<div>{@html data.post.content}</div>

{#if next}
	<p>Next post: <a href="/blog/{next.slug}">{next.title}</a></p>
{/if}