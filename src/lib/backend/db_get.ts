import { supabase } from "$lib/backend/supabaseClient";
import type { UUID } from "crypto";


export async function all_courses() {
    
    let { data, error } = await supabase
      .from('all_courses')
      .select('*')
      .order('order', {ascending: true});
  
      return{
        courses: data ?? []
      }
  }

  export const get_course = async(name:String) =>{
    let {data, error} = await supabase
        .from("all_courses")
        .select("*")
        .eq("name", name)

    return{
        course: data ?? []
    }
  }


  export const get_user_data = async() =>{

    let user:any = await get_current_user()
    
    

    let {data, error} = await supabase
    .from("user_data")
    .select("*")
    .eq("id", user?.id)

    return{
        user_data: data ?? []
    }
  }

  export const get_current_user = async() =>{
    const { data: { user } } = await supabase.auth.getUser()

    console.log(user)

    return user
  }