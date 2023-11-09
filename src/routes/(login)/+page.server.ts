import { all_courses_names } from "$lib/backend/sample/test";
import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = async () => {
    let names = await all_courses_names()

    return {
        names: names
    };

}
