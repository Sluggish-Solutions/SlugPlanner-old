import { error } from '@sveltejs/kit'
import type { PageServerLoad } from './$types'

// example: pulls data from database
// import * as db from '$lib/server/database';
// export const load: PageServerLoad = ({ params }) => {
// 	return {
// 		post: await db.getPost(params.slug),
// 	}
// }

// /** @type {import('./$types').PageServerLoad} */
// export function load({ params }) {
export const load: PageServerLoad = ({ params }) => {
	return {
		post: {
			title: `Course: ${params.slug}`,
			content: `<b>Content for ${params.slug} goes here</b>`,
		},
	}
	// throw error(404, 'Not found here')
}
