<script lang="ts">
	import type { LayoutData } from './$types'

	import * as Collapsible from '$lib/components/ui/collapsible'
	import { ChevronsUpDown } from 'lucide-svelte'
	import { Button } from '$lib/components/ui/button'

	export let data: LayoutData

	let groupedData: any = []
	let prefix = 'AM'
	let classTypes: Array<String> = []

	const group = () => {
		let groupClasses: any = []
		data.courses.courses.forEach((course) => {
			if (prefix == course.name.split(' ')[0]) {
				groupClasses.push(course)
			} else {
				groupedData.push(groupClasses)
				groupClasses = []
				classTypes.push(prefix)
				prefix = course.name.split(' ')[0]
			}
		})
	}
	group()
	console.log(groupedData)
	console.log(classTypes)
</script>

<div class="flex">
	<aside id="sidebar" class="">
		{#each classTypes as classType, index}
			<Collapsible.Root class="w-[350px] space-y-2">
				<Collapsible.Trigger asChild let:builder>
					<Button
						builders={[builder]}
						variant="ghost"
						size="lg"
						class="w-60"
					>
						{classType}</Button
					>
				</Collapsible.Trigger>
				<Collapsible.Content class="ml-9 space-y-2">
					{#each groupedData[index] as course}
						<a href="/class/{course.name}">
							<div class="rounded-md border text-center px-4 py-3 w-60 ml-9 font-mono text-sm">
								{course.name}
							</div>
<!-- 
							<Button variant="ghost" size="lg" class="w-60">
								{course.name}</Button
							> -->
						</a>
					{/each}
				</Collapsible.Content>
			</Collapsible.Root>
		{/each}
	</aside>

	<main id="main-section" class="flex justify-center">
		<slot />
	</main>
</div>

<style>
	#sidebar {
	}

	#main-section {
	}
</style>
