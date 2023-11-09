import { supabase } from "$lib/backend/supabaseClient";

export async function all_courses_names() {

    let { data, error } = await supabase
    .from('all_courses')
    .select('name')

  return {
    courses: data ?? []
  };
}

export async function all_courses() {
  let { data, error } = await supabase
    .from('all_courses')
    .select('*')

    return{
      courses: data ?? []
    }
}

