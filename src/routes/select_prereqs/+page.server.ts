import type { PageServerLoad } from './$types'
import {
	get_user_data,
	get_current_user,
	all_courses,
} from '$lib/backend/db_get'

export const load: PageServerLoad = async ({ params }) => {
	return {
	  courses: await all_courses(),
		user: await get_current_user(),
		user_data: await get_user_data(),
	}
}
