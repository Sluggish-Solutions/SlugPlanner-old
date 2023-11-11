<script lang="ts">
	import type { LayoutData } from './$types'

	import * as Collapsible from '$lib/components/ui/collapsible'
	import { ChevronLeft, ChevronDown } from 'lucide-svelte'
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
	// console.log(data.courses)
	// console.log(groupedData)
	// console.log(classTypes)
</script>

<div class="flex">
	<aside
		id="sidebar"
		class="p-5 min-w-min rounded-md bg-slate-100 m-9 h-[73vh] overflow-x-hidden overflow-y-hidden"
	>
		{#each classTypes as classType, index}
			<Collapsible.Root class=" w-40 space-y-2 overflow-y-scroll">
				<Collapsible.Trigger asChild let:builder>
					<Button
						builders={[builder]}
						variant="ghost"
						size="lg"
						class="w-36 text-right bg-slate-50 hover:bg-blue-100 {builder[
							'data-state'
						] == 'open'
							? `bg-blue-300`
							: ''}"
					>
						<!-- remove color in closed state -->
						<div class="flex w-full justify-between">
							<!-- Class Types show here. -->
							{classType}

							{#if builder['data-state'] == 'open'}
								<span class="flex">
									<ChevronDown class="h-4 w-8" />
								</span>
							{:else}
								<span class="flex">
									<ChevronLeft class="h-4 w-8" />
								</span>
							{/if}
						</div>
					</Button>
				</Collapsible.Trigger>

				<Collapsible.Content class="ml-3 space-y-2">
					{#each groupedData[index] as course}
						<a href="/class/{course.name}" class=" w-32 rounded-md">
							<div
								class="rounded-md border px-4 py-3 font-mono text-center text-sm w-full bg-slate-50"
							>
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
