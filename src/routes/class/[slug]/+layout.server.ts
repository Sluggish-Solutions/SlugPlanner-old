import type { LayoutServerLoad } from './$types'
import { all_courses } from '$lib/backend/db_get'

// /** @type {import('./$types').LayoutServerLoad} */
export const load: LayoutServerLoad = async () => {
	console.log('hello');
	
	return {
		// posts: await db.getPostSummaries()
		// posts: [{slug: 'nyt', title: 'New York Times'}, {slug: 'wsj', title: 'Wall Street Journal'}]
		courses: await all_courses(),
	}
}
