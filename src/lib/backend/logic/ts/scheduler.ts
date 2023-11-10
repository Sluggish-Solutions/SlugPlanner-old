import { supabase } from "$lib/backend/supabaseClient";
import { all_courses } from "$lib/backend/db_get";
// Assuming response is a list of dictionaries

export const data_fetch = async() =>{
    return await all_courses()
}

let data: any = data_fetch()

console.log(data)
console.log("hhi")


// const weird_shit: any = response.data;

// const ordered_classes: any[] = JSON.parse(JSON.stringify(weird_shit));

// console.log(typeof ordered_classes);

// const list_of_classes: Record<string, any> = {};
// for (const i of ordered_classes) {
//   const name: string = i.name;
//   list_of_classes[name] = i;
// }

// // START OF LOGIC
// const major: string = 'CS';
// const prereq: string[] = ['AP C BC 3', 'CSE 20', 'WRIT 1'];

// function prereq_check(prereq: string[], desired_class: string): boolean {
//   let flag: boolean = true;
//   for (const i of list_of_classes[desired_class]) {
//     // Your logic here
//   }
//   if (major === 'CS') {
//     // Your additional logic here
//   }
//   return flag;
// }

// // Add any additional TypeScript-specific logic as needed
