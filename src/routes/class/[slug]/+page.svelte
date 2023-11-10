<script lang="ts">
	// /** @type {import('./$types').PageData} */
	import type { PageData } from './$types'
	export let data: PageData
	import * as Collapsible from '$lib/components/ui/collapsible'
	import { ChevronsUpDown } from 'lucide-svelte'
	import { Button } from '$lib/components/ui/button'

	import { page } from '$app/stores'
	// we can access `data.posts` because it's returned from
	// the parent layout `load` function
	// $: index = data.courses.findIndex(post => post.slug === $page.params.slug);
	// $: next = data.posts[index + 1] || data.posts[index - 1];
	console.log(data.course[0])

	$: course = {
		name: data.course[0].name,
		title: data.course[0].info.title,
		description: data.course[0].info.description,
		class_notes: data.course[0].info.class_notes,
		quarters: data.course[0].info.quarters_offered
			.map((word: String) => word.charAt(0).toUpperCase() + word.slice(1))
			.join(', '),
		ge_code: data.course[0].info.gen_ed_code,
		// pre_reqs: data.course[0].info.pre_reqs,
	}

	// for (var i in course.pre_reqs) {
	// 	console.log(course.pre_reqs[i])
	// }
</script>

<div class="text-lg space-y-3">
	<h1
		class="font-bold text-2xl p-5 pl-9 underline decoration-blue-500 decoration-4"
	>
		{course.name} : {course.title}
	</h1>
	<p>
		<mark class="p-1 px-2 underline decoration-2 rounded-md font-bold"
			>Description</mark
		>
		: {course.description}
	</p>

	{#if course.class_notes != 'NULL'}
		<p class="">
			<mark class="p-1 px-2 underline decoration-2 rounded-md font-bold"
				>Notes</mark
			>
			: {course.class_notes}
		</p>
	{/if}
	<!-- {#if course.pre_reqs != 'NULL'} -->
		<p class="">
			<mark class="p-1 px-2 underline decoration-2 rounded-md font-bold"
				>Prereqs</mark
			>
			<!-- {#each course.pre_reqs as pre_reqs} -->
				<!-- : {console.log(course.pre_reqs[1])} -->
			<!-- {/each} -->
		</p>
	<!-- {/if} -->
	<p>
		<mark class="p-1 px-2 underline decoration-2 rounded-md font-bold"
			>Quarters</mark
		>
		: {course.quarters}
	</p>
	<p>
		<mark class="p-1 px-2 underline decoration-2 rounded-md font-bold"
			>GE Code</mark
		>
		{#if course.ge_code != 'NULL'}
			: {course.ge_code}
		{:else}
			: None
		{/if}
	</p>

	<Collapsible.Root class="w-[300px] space-y-2">
		<div class="flex items-center justify-between px-4">
			<h4 class="text-sm font-semibold">Show More</h4>
			<Collapsible.Trigger asChild let:builder>
				<Button
					builders={[builder]}
					variant="ghost"
					size="sm"
					class="w-9 p-0"
				>
					<span class="flex">
						<ChevronsUpDown class="h-4 w-8" />
					</span>
				</Button>
			</Collapsible.Trigger>
		</div>
		<Collapsible.Content class="space-y-2">
			<div class="rounded-md border px-4 py-3 font-mono text-sm">
				bits-ui
			</div>
			<div class="rounded-md border px-4 py-3 font-mono text-sm">
				@radix-ui/primitives
			</div>
		</Collapsible.Content>
	</Collapsible.Root>
</div>
<!-- {#if data.course.pre_reqs}
	<p>Next post: <a href="/blog/{next.slug}">{next.title}</a></p>
{/if} -->
