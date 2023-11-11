import type { PageServerLoad } from './$types'
import { get_course } from '$lib/backend/db_get'
import { error, redirect } from '@sveltejs/kit'

export const load: PageServerLoad = async ({ params }) => {
	try {
		return await get_course(params.slug)
	} catch  {
		throw redirect(300, "/")
	}


}
