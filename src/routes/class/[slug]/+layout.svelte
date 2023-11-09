<script lang="ts">
	import type { LayoutData } from './$types'
	export let data: LayoutData

	// interface Course {
	// 	name: string
	// 	title
	// 	description
	// 	prereq
	// }

	let groupedData: Array<Course> = []
	let prefix = ''

	const group = () => {
		data.courses.courses.forEach((course) => {
			if (prefix == course.name.split(' ')[0]) {
				groupedData.push(course)
			} else {
				prefix = course.name.split(' ')[0]
				groupedData.push(prefix)
				groupedData.push(course)
			}
		})
	}
	group()
	console.log(groupedData[1])
</script>

<div class="flex">
	<aside id="sidebar" class="flex justify-center">
		<h2>More posts:</h2>
		<ul>
			{#each groupedData as course}
				{#if typeof course == 'string'}
					<h1 class="text-2xl">{course}</h1>
				{:else}
					<li><a href="/class/{course.name}">{course.name}</a></li>
				{/if}
			{/each}
			<!-- {#each data.courses.courses as course}
			{#if course.name.split(' ')[0] == classType}
				<p>{course.name.split(' ')[0]}</p>
				<p>Hi, {classType}</p>
			{:else}
				{classType = course.name.split(' ')[0]}
				<h1>changed to {classType}, {course.name}</h1>
				<p>HIERER</p>
			{/if}
		{/each} -->
		</ul>
	</aside>

	<main id="main-section" class="flex justify-center">
		<slot />
	</main>
</div>

<style>
	#sidebar {
		width: 30%;
		flex-grow: 1;
	}

	#main-section {
		width: 70%;
		flex-grow: 1;
	}
</style>
