import type { LayoutServerLoad } from './$types'

// /** @type {import('./$types').LayoutServerLoad} */ 
export const load: LayoutServerLoad = () => {
	return {
		// posts: await db.getPostSummaries()
		posts: [{slug: 'nyt', title: 'New York Times'}, {slug: 'wsj', title: 'Wall Street Journal'}]
	}
}
