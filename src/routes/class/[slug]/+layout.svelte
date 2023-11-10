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
						class="w-72"
					>
						{classType}</Button
					>
				</Collapsible.Trigger>
				<Collapsible.Content class="space-y-2">
					{#each groupedData[index] as course}
						<div class="rounded-md border px-4 py-3 font-mono text-sm">
							{course.name}
						</div>
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
		width: 30%;
		flex-grow: 1;
	}

	#main-section {
		width: 70%;
		flex-grow: 1;
	}
</style>
