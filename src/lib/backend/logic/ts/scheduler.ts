import { supabase } from "$lib/backend/supabaseClient";
import { all_courses, get_course} from "$lib/backend/db_get";
// Assuming response is a list of dictionaries

export const data_fetch = async() =>{


    return await all_courses()



}
export const course_fetch = async(params:string) =>{


    return await get_course(params)
}

let data: any = await data_fetch()


 const list_of_classes: Record<string, any> = {};

 // START OF LOGIC
 const major: string = 'CS';
 const user_prereq: string[] = ['AP C BC 3', 'CSE 20', 'WRIT 1', 'AM 10'];

 const prereq_check = async( desired_class: string) => {
   let flag: boolean = true;
   let flag_internal: boolean = false;
   let course_data = await course_fetch(desired_class)
   let course_prereq = Object.values(course_data.course[0].info.pre_reqs).filter((child) => Array.isArray(child))
   console.log(course_prereq)
   for (const i of course_prereq) {
   //   Your logic here
        for(const j of i){
            for(const q of user_prereq){
                if (q == j){
                    flag_internal = true
                }
            }
        }
        console.log(flag_internal)
        if(!flag_internal){
            flag = false
            console.log(flag)

        }
        flag_internal = false

   }
   console.log(flag)
   return flag

//    if (major === 'CS') {
//      // Your additional logic here
//    }
//    return flag;
 }
 await prereq_check('AM 30')

  //Add any additional TypeScript-specific logic as needed
