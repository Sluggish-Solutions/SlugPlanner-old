import { signOutUser } from '$lib/backend/auth';
import type { PageLoad } from './$types';

export const load = (async () => {

    let response:any =  await signOutUser()

    if (response == "success"){
        return {status: true}
    }
    return {status :false}

}) satisfies PageLoad;