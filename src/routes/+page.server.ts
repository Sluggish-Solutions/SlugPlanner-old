import { supabase } from "$lib/backend/supabaseClient";

export async function load() {

    
    let { data, error } = await supabase
    .from('all_courses')
    .select('*')

  console.log(data?.length)
  return {
    courses: data ?? []
  };
}