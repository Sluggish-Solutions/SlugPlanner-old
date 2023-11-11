import { get_current_user, get_user_data } from "$lib/backend/db_get";
// import type { PageServerLoad } from "./$types";

export const load = (async () => {
  let user: any = await get_current_user();

  return {user};
})
