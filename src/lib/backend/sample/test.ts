import { supabase } from "$lib/backend/supabaseClient";

export async function all_courses_names() {

    let { data, error } = await supabase
    .from('all_courses')
    .select('name')

  return {
    courses: data ?? []
  };
}