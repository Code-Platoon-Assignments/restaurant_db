/**
 * Lists 10 course names and ids.
 * This is here for "hello world" & testing purposes to confirm everything works.
 */
function listCourses() {
  /**  here pass pageSize Query parameter as argument to get maximum number of result
   * @see https://developers.google.com/classroom/reference/rest/v1/courses/list
   */
  const optionalArgs = {
    pageSize: 10
    // Use other parameter here if needed
  };
  try {
    // call courses.list() method to list the courses in classroom
    const response = Classroom.Courses.list(optionalArgs);
    const courses = response.courses;
    if (!courses || courses.length === 0) {
      console.log('No courses found.');
      return;
    }
    // Print the course names and IDs of the courses
    for (const course of courses) {
      console.log('%s (%s)', course.name, course.id);
      console.log(course);
    }
  } catch (err) {
    // TODO (developer)- Handle Courses.list() exception from Classroom API
    // get errors like PERMISSION_DENIED/INVALID_ARGUMENT/NOT_FOUND
    console.log('Failed with error %s', err.message);
  }
}  

/***
 * A hello world function you can run to make sure everything works.
 */
const greeter = (person: string) => {
    return `Hello, ${person}!`;
  }
  
  function testGreeter() {
    const user = 'Grant';
    Logger.log(greeter(user));
  }
