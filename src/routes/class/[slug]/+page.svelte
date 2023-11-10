<script lang="ts">
	// /** @type {import('./$types').PageData} */
	import type { PageData } from './$types'
	export let data: PageData

	import { page } from '$app/stores'
	// we can access `data.posts` because it's returned from
	// the parent layout `load` function
	// $: index = data.courses.findIndex(post => post.slug === $page.params.slug);
	// $: next = data.posts[index + 1] || data.posts[index - 1];
</script>

<h1>`{console.log(data)}: {data.course.title}`</h1>

<!-- {#if data.course.pre_reqs}
	<p>Next post: <a href="/blog/{next.slug}">{next.title}</a></p>
{/if} -->
