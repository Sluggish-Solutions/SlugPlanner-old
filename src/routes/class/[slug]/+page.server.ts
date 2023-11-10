import type { PageServerLoad } from './$types'
import { get_course } from '$lib/backend/db_get'

export const load: PageServerLoad = async ({ params }) => {
	return {
		course: await get_course(params.slug)
	}
}
