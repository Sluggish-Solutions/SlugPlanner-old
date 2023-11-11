import { supabase } from "$lib/backend/supabaseClient";
import { all_courses, get_course } from "$lib/backend/db_get";
// Assuming response is a list of dictionaries

let data: any = await all_courses();

const list_of_classes: Record<string, any> = {};

// START OF LOGIC
const major: string = "CE";
// const user_prereq: string[] = ["AP C BC 3", "CSE 20", "WRIT 1", "AM 10"];


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

// let mainArray: Set<String>[] = [
//   new Set<String>([
//     "CSE 102",
//     "CSE 150",
//     "CSE 113",
//     "CSE 185E",
//     "CSE 121",
//     "CSE 115C",
//     "CSE 107",
//   ]),
// ];

// mainArray.push(topSet);

// if (major == 'CE')
// export const scheduler = async () => {
//   //   while (pre_req_exists) {

//   let current_classes = [];
//   let layered_set = new Set<String>();
//   //   let current_set = mainArray[mainArray.length - 1];

//   for (let cur_set_index = 0; cur_set_index < 8; cur_set_index++) {
//     for (let course_name of mainArray[cur_set_index]) {
//       let course_data = await get_course(course_name);
//       let course_prereqs = Object.values(
//         course_data.course[0].info.pre_reqs
//       ).filter((child) => Array.isArray(child));
//       //parse throuh pre-req and add if we want to
//       // for (let pre_req_arr of course_prereqs) {
//       //   layered_set.add(pre_req_arr[0]);
//       // }
//       // if (cur_set_index == 1) {
//       //   return { layered_set };
//       // }
//     }
//     mainArray.push(new Set(layered_set));
//     layered_set.clear();
//   }

//   return { mainArray };
// };

function arraysAreEqual(arr1: any[], arr2: any[]): boolean {
  // Check if arrays have the same length
  if (arr1.length !== arr2.length) {
      return false;
  }

  // Check each element for equality
  for (let i = 0; i < arr1.length; i++) {
      if (arr1[i] !== arr2[i]) {
          return false;
      }
  }

  // Arrays are equal
  return true;
}

export const scheduler = async () => {
  return await get_pre_reqs();
};

const get_pre_reqs = async () => {
  let looping: boolean = true;
  let mainArray: Array<Array<string>> = [
    [
      "CSE 102",
      "CSE 150",
      "CSE 113",
      "CSE 185E",
      "CSE 121",
      "CSE 115C",
      "CSE 107",
    ],
  ];

  let count: number = 0;
  while (looping) {
    

    let new_arr: Array<string> = [];
    let layered_set = new Set(); // Create a new Set for each iteration
    // mainArray.length = 1
    let course_set = mainArray[mainArray.length - 1]; // course_set = ["CSE 102", "CSE 150", "CSE 113", "CSE 185E", "CSE 121", "CSE 115C", "CSE 107"]

    // return { course_set }
    for (let j: number = 0; j < course_set.length; j++) {
      // course_set.length = 7
      let course_name = Array.from(course_set)[j]; // course_name = "CSE 102"
      let course_data = await get_course(course_name); // course_data = { course: [ { info: { pre_reqs: { '0': [Array], '1': [Array], '2': [Array], '3': [Array], '4': [Array], '5': [Array], '6': [Array] } } } ] }

      if (course_data.length == 0) {
        // if course_data is empty, skip
        continue;
      }

      let course_prereqs: any;
      try {
        course_prereqs = Object.values(
          course_data.course[0].info.pre_reqs
        ).filter((child) => Array.isArray(child));
      } catch {
        // return {"hello": "wtf"}
        continue;
      }
      layered_set.add(course_prereqs);
    }

    for (let k: number = 0; k < layered_set.size; k++) {
      let some_arr: any = Array.from(layered_set)[k];
      // return { some_arr }
      for (let l = 0; l < some_arr.length; l++) {
        new_arr.push(some_arr[l][0]);
      }
    }

    let arr_set = Array.from(new Set(new_arr));

    if (arr_set.length == 0 || count > 12) {
      looping = false;
    } else {

      let last_arr = mainArray[mainArray.length -1]

      if (arraysAreEqual(last_arr, arr_set.sort())){
        looping = false
      }else{

      mainArray.push(arr_set.sort());
    }
  }








    count += 1;
  }

  return { mainArray };
  // if (arr_set.length == 0) {
  //   return { mainArray };
  // }
  // return get_pre_reqs(mainArray.push(arr_set));
  // for (let k = 0; i < course_prereqs.size; k++) {
  //   return { course_prereqs };
  // layered_set.add(course_prereqs[k][0]);
  // layered_set.add(pre_req_arr[0]);
};

// end of while loop: if new set of pre-req classes is null, or all satisfied, then pre_req_exists = false and while loop stops
