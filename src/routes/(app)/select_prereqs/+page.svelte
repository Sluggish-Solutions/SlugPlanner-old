<script lang="ts">
	import type { PageData } from './$types'

	import * as Collapsible from '$lib/components/ui/collapsible'
	import { ChevronDown, ChevronLeft } from 'lucide-svelte'
	import { Button } from '$lib/components/ui/button'

	export let data: PageData

	let groupedData: any = []
	let prefix = 'AM'
	let classTypes: Array<String> = []
	let updateList = () => {
		console.log('clicked')
	}

	const group = () => {
		let groupClasses: any = []
		data.courses.courses.forEach((course) => {
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

<aside
	id="sidebar"
	class="p-5 min-w-min rounded-md bg-slate-100 m-9 h-[70vh] overflow-x-scroll flex"
>
	{#each classTypes as classType, index}
		<Collapsible.Root class=" w-40 space-y-2">
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

			<Collapsible.Content class="space-y-1">
				{#each groupedData[index] as course}
						<button
							class="rounded-md border px-1 py-2 font-mono text-center text-sm w-full bg-slate-50 active:bg-slate-100" on:click={updateList}
						>
							{course.name}
						</button>
				{/each}
			</Collapsible.Content>
		</Collapsible.Root>
	{/each}
</aside>
