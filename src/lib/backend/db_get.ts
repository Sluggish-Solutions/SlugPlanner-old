import { supabase } from "$lib/backend/supabaseClient";


export async function all_courses() {
    
    let { data, error } = await supabase
      .from('all_courses')
      .select('*')
      .order('order', {ascending: true});
  
      return{
        courses: data ?? []
      }
  }

  export const get_course = async(name:string) =>{
    let {data, error} = await supabase
        .from("all_courses")
        .select("*")
        .eq("name", name)
  }

