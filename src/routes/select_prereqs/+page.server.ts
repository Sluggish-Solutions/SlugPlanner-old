import type { PageServerLoad } from "./$types";
import { get_user_data, get_current_user } from "$lib/backend/db_get";

export const load: PageServerLoad = async ({ params }) => {
  let user: any = await get_current_user();

  return await get_user_data();
};
