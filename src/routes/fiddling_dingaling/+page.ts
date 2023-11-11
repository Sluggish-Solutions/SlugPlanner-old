import { data_fetch } from '$lib/backend/logic/ts/scheduler';
import type { PageLoad } from './$types';

export const load = (async () => {
    return await data_fetch()

}) satisfies PageLoad;