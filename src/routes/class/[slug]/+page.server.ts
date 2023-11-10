import type { PageServerLoad } from './$types'
import { get_course } from '$lib/backend/db_get'

export const load: PageServerLoad = async ({ params }) => {
	return await get_course(params.slug)
}
