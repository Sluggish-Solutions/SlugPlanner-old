import { get_current_user, get_user_data } from "$lib/backend/db_get";
import type { PageLoad } from "./$types";

export const load = (async () => {
  let user: any = await get_current_user();

  // console.log(user);


  return {user};
}) satisfies PageLoad;
