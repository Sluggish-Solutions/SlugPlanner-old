import { data_fetch } from '$lib/backend/logic/ts/scheduler';
import type { PageLoad } from './$types';

export const load = (async () => {
    let blah: any = await data_fetch()

    return {blah};
}) satisfies PageLoad;