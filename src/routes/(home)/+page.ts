import { get_current_user, get_user_data } from "$lib/backend/db_get";
import type { PageLoad } from "./$types";

export const load = (async () => {
  let user_data: any = await get_user_data();

  console.log(user_data);

  return {};
}) satisfies PageLoad;
