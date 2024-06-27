# University Course Management System
Design Overview: The program contains classes and functions for conducting university activities such as adding students, instructors, courses, attendance monitoring, and grading. The primary elements are:

Dataclasses: Student, Course, and Instructor represent the core entities with relevant attributes.

1. Enums: GradeLevelEnum, CourseStatusEnum, and GradeStatusEnum define predefined categories like grade levels, course statuses, and grades.

2. CourseManagement Class: Organises tasks such as adding/updating students, teachers, and courses, tracking attendance, and assigning grades. It also manages file I/O for fixed data storage.

Usage Guide:

1. Adding/Updating Students and Instructors:
   Use add_student(name, grade, address, phone) and add_instructor(name, subject, email) respectively.
   Update student/instructor details with update_student(student_id, ...) and update_instructor(instructor_id, ...).

2. Managing Courses:
   Add courses with add_course(course_code, title, credits, instructor_id, status) and change their status using change_course_status(course_code, new_status).
   Assign instructors to courses via assign_instruct_to_course(course_code, instructor_id).

3. Attendance and Grades:
   Record attendance with take_attendance(student_id, status) and assign grades using assign_std_grades(student_id, course_code, grade).
   Retrieve all grades with get_all_grades().

4. Getting Information:
   Obtain student/instructor details with get_student_info(student_id) and get_all_instructors_info().
   Retrieve all students/courses info with get_all_students_info() and get_all_courses_info().

5. File Operate:
   Student IDs, instructor IDs, and course data are stored in respective files for persistent data handling.
