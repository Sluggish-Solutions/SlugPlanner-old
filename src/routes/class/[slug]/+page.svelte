<script lang="ts">
	import type { PageData } from './$types'

	export let data: PageData

	// check if course exists
	$: console.log(data)

	$: course = {
		name: data.course[0].name,
		title: data.course[0].info.title,
		description: data.course[0].info.description,
		class_notes: data.course[0].info.class_notes,
		quarters: data.course[0].info.quarters_offered
			.map((word: String) => word.charAt(0).toUpperCase() + word.slice(1))
			.join(', '),
		ge_code: data.course[0].info.gen_ed_code,
		pre_reqs: data.course[0].info.pre_reqs,
		type: data.course[0].info.type,
	}

	// gets number of pre_reqs
	$: pre_req_len = Object.values(course.pre_reqs).filter((child) =>
		Array.isArray(child)
	).length

	// $: console.log(
	// 	Object.values(course.pre_reqs).filter((child) => Array.isArray(child))
	// )
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
		:
		{#if pre_req_len != 0}
			{#each Array(pre_req_len) as _, i (i)}
				{#each course.pre_reqs[i] as pre_req, k}
					{#if isNaN(parseInt(pre_req[0]))}
						<a href="/class/{pre_req}">
							{pre_req}
						</a>
					{:else}
						Math Placement {pre_req}
					{/if}
					{#if k != course.pre_reqs[i].length - 1}
						or
					{/if}
				{/each};&nbsp
			{/each}
		{:else}
			None
		{/if}
	</p>
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
</div>
<!-- {#if data.course.pre_reqs}
	<p>Next post: <a href="/blog/{next.slug}">{next.title}</a></p>
{/if} -->
