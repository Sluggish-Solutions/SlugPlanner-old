import { scheduler } from '$lib/backend/logic/ts/scheduler';
import type { PageLoad } from './$types';

export const load = (async () => {
    return await scheduler()    

}) satisfies PageLoad;