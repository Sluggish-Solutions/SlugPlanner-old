import { supabase } from "$lib/backend/supabaseClient";
import { all_courses, get_course } from "$lib/backend/db_get";
// Assuming response is a list of dictionaries

let data: any = await all_courses();

const list_of_classes: Record<string, any> = {};

// START OF LOGIC
const major: string = "CE";
const user_prereq: string[] = ["AP C BC 3", "CSE 20", "WRIT 1", "AM 10"];

// export const prereq_check = async (desired_class: string) => {
// 	let flag: boolean = true
// 	let flag_internal: boolean = false
// 	let course_data = await course_fetch(desired_class)
// 	let course_prereq = Object.values(
// 		course_data.course[0].info.pre_reqs
// 	).filter((child) => Array.isArray(child))
// 	console.log(course_prereq)
// 	for (const i of course_prereq) {
// 		//   Your logic here
// 		for (const j of i) {
// 			for (const q of user_prereq) {
// 				if (q == j) {
// 					flag_internal = true
// 				}
// 			}
// 		}
// 		console.log(flag_internal)
// 		if (!flag_internal) {
// 			flag = false
// 			console.log(flag)
// 		}
// 		flag_internal = false
// 	}
// 	console.log(flag)
// 	return flag

// }
// await prereq_check('AM 30')

// //Add any additional TypeScript-specific logic as needed

let pre_req_exists = true;

let mainArray: Set<String>[] = [];
const topSet = new Set<String>([
  "CSE 102",
  "CSE 150",
  "CSE 113",
  "CSE 185E",
  "CSE 121",
  "CSE 115C",
  "CSE 107",
]);
mainArray.push(topSet);

// if (major == 'CE')
export const scheduler = async () => {
  //   //   while (pre_req_exists) {
  //   let current_set = mainArray[mainArray.length - 1];
  //   for (let course in current_set) {
  //     let course_data = await get_course(course);
  //     // array of course_pre_reqs
  //     let course_prereq = Object.values(
  //       course_data.course[0].info.pre_reqs
  //     ).filter((child) => Array.isArray(child));
  //  return mainArray;
  return { mainArray };
  //   }
  //   }
};

// end of while loop: if new set of pre-req classes is null, or all satisfied, then pre_req_exists = false and while loop stops
