/**
 * Run this to look at the JSON object w/ids, names, calendar ids, etc, for each course.
 * You can also use typescript type hints.
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
      return [];
    }

    // Print the course names and IDs of the courses
    for (const course of courses) {
      console.log('%s (%s)', course.name, course.id);
      console.log(course);
    }

    return courses;
  } catch (err) {
    // TODO (developer)- Handle Courses.list() exception from Classroom API
    // get errors like PERMISSION_DENIED/INVALID_ARGUMENT/NOT_FOUND
    const errorMsg = ('Failed with error %s', err.message);
    console.log(errorMsg);
    return errorMsg;
  }
}

function getCourse(courseId: GoogleAppsScript.Classroom.Schema.Course["id"]) {
  const course = Classroom.Courses.get(courseId);
  console.log(`Got course - ${course.name} ${course.descriptionHeading} - id - ${course.id}`);
  return course;
}

function getCourseTopics(course: GoogleAppsScript.Classroom.Schema.Course) {
  return Classroom.Courses.Topics.list(course.id);
}

function getCourseAssignments(course: GoogleAppsScript.Classroom.Schema.Course) {
  return Classroom.Courses.CourseWork.list(course.id);
}

// See https://developers.google.com/classroom/guides/manage-topics
// API docs: https://developers.google.com/classroom/reference/rest/v1/courses.topics
function createTopic(course: GoogleAppsScript.Classroom.Schema.Course, name: string) {
  try {
    return Classroom.Courses.Topics.create({ name }, course.id);
  } catch (err) {
    return err;
  }
}

// See https://developers.google.com/classroom/guides/manage-coursework
// API reference: https://developers.google.com/classroom/reference/rest/v1/courses.courseWork
function createAssignment(course: GoogleAppsScript.Classroom.Schema.Course) {
  const courseWork: GoogleAppsScript.Classroom.Schema.CourseWork = {
    'title': 'Ant colonies',
    'description': 'Read the article about ant colonies and complete the quiz.',
    'materials': [
      { 'link': { 'url': 'http://example.com/ant-colonies' } },
      { 'link': { 'url': 'http://example.com/ant-quiz' } }
    ],
    'workType': 'ASSIGNMENT',
    'state': 'PUBLISHED',
  };

  try {
    return Classroom.Courses.CourseWork.create(courseWork, course.id);
  } catch (err) {
    return err;
  }
}

/***
 * Helper functions 
 */

// Create an assignment
function createTestCourseAssignment() {
  return createAssignment(getTestCourse());
}

// Create a topic
function createTestCourseTopic() {
  return createTopic(getTestCourse(), "Yet another API generated Topic");
}

// Get a specific google classroom (course)
function getTestCourse() {
  return getCourse('522784645757');
}

function getTangoPlatoon() {
  return getCourse('576555342077');
}

function getUniformPlatoon() {
  return getCourse('612339173048');
}

// Get all coursework for a specific course
function getTestCourseAssignments() {
  return getCourseAssignments(getTestCourse());
}

function getTangoAssignments() {
  return getCourseAssignments(getTangoPlatoon());
}

// Get all topics for a specific course
function getTestCourseTopics() {
  return getCourseTopics(getTestCourse());
}

function getTangoTopics() {
  return getCourseTopics(getTangoPlatoon());
}

// Create 


/***
 * hello world functions you can run to make sure everything works.
 */
const helloWorld = (person: string) => {
  return `Hello, ${person}!`;
}

function testHelloWorld() {
  const msg = helloWorld('Grant');
  Logger.log(msg);
  return msg;
}
