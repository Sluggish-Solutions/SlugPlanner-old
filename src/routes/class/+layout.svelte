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
		data.courses.forEach((course) => {
			if (prefix != course.name.split(' ')[0]) {
				groupedData.push(groupClasses)
				groupClasses = []
				classTypes.push(prefix)
				prefix = course.name.split(' ')[0]
			}
			groupClasses.push(course)
		})
	}
	group()
	console.log(data.courses)
	// console.log(groupedData)
	// console.log(classTypes)
</script>

<div class="flex gap-3">
	<aside id="sidebar" class="p-3 min-w-min rounded-md bg-slate-100 m-9 h-[90vh] overflow-y-scroll">
		{#each classTypes as classType, index}
			<Collapsible.Root class="w-[200px] space-y-2">
				<Collapsible.Trigger asChild let:builder>
					<Button
						builders={[builder]}
						variant="ghost"
						size="lg"
						class="w-36 text-right bg-slate-50"
					>
						{classType}</Button
					>
				</Collapsible.Trigger>
				<Collapsible.Content class="ml-5 space-y-2">
					{#each groupedData[index] as course}
						<a href="/class/{course.name}">
							<div class="rounded-md border px-4 py-3 text-center w-36 font-mono text-sm">
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

	<main id="main-section" class="py-11 px-7 mr-14">
		<slot />
	</main>
</div>

<style>
	#sidebar {
	}

	#main-section {
	}
</style>
