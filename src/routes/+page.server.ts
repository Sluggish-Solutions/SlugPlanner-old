import { all_courses_names } from "$lib/backend/sample/test";
export async function load() {
    try {
      console.log('Fetching courses...');
      const courses = await all_courses_names();
      console.log('Courses:', courses);
      return {
         courses 
      };
    } catch (error) {
      console.error('Error fetching courses:', error);
      return {
        status: 500,
        error: new Error('Failed to load courses')
      };
    }
  }