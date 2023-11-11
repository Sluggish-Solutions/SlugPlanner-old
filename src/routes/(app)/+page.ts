import { get_current_user, get_user_data, get_user_schedule } from "$lib/backend/db_get";
// import type { PageServerLoad } from "./$types";

export const load = (async () => {
  let user: any = await get_current_user()
  let saved_schedule: any = await get_user_schedule();

  saved_schedule = saved_schedule
  return {saved_schedule, user};
})
