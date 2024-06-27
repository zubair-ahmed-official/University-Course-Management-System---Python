"""
7.5DN Custom Program
"""
__author__ = "ZUBAIR AHMED" 

import university_process as up

def adding_student(cm):
    """
    Adds a new student.
    """
    name = input("Enter student name: ")
    grade = up.GradeLevelEnum(int(input("Enter grade level (0-Freshman, 1-Sophomore, 2-Junior, 3-Senior): ")))
    address = input("Enter address: ")
    phone = input("Enter phone: ")
    student_id, msg = cm.add_student(name, grade, address, phone)
    print(f"{msg} - Student ID: {student_id}")
    
def updating_student(cm):
    """
    Updates student information.
    """
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    grade = up.GradeLevelEnum(int(input("Enter grade level (0-Freshman, 1-Sophomore, 2-Junior, 3-Senior): ")))
    address = input("Enter address: ")
    phone = input("Enter phone: ")
    student_id, msg = cm.update_student(student_id, name, grade, address, phone)
    print(msg)
    
def removing_student(cm):
    """
    Removes a student.
    """
    student_id = int(input("Enter student ID to remove: "))
    cm.remove_student(student_id)
    print("Student removed successfully")
    
def adding_instructor(cm):
    """
    Adds a new instructor.
    """
    name = input("Enter instructor name: ")
    subject = input("Enter subject: ")
    email = input("Enter email: ")
    instructor_id, msg = cm.add_instructor(name, subject, email)
    print(f"{msg} - Instructor ID: {instructor_id}")
    
def updating_instructor(cm):
    """
    Updates instructor information.
    """
    instructor_id = int(input("Enter instructor ID: "))
    name = input("Enter instructor name: ")
    subject = input("Enter subject: ")
    email = input("Enter email: ")
    instructor_id, msg = cm.update_instructor(instructor_id, name, subject, email)
    print(msg)
    
def adding_course(cm):
    """
    Adds a new course.
    """
    course_code = input("Enter course code: ")
    title = input("Enter course title: ")
    credits = int(input("Enter number of credits: "))
    instructor_id = int(input("Enter instructor ID: "))
    status = input("Enter status: ")
    result_code, result_msg = cm.add_course(course_code, title, credits, instructor_id, status)
    print(result_msg)
    
def changing_course_status(cm):
    """
    Changes the status of a course.
    """
    course_code = input("Enter course code: ")
    status = up.CourseStatusEnum(int(input("Enter course status (0-Active, 1-Inactive, 2-Upcoming): ")))
    result = cm.change_course_status(course_code, status)
    if result != -1:
        print("Course status changed successfully")
    else:
        print("Course not found")
        
def instructor_to_course(cm):
    """
    Assigns an instructor to a course.
    """
    course_code = input("Enter course code: ")
    instructor_id = int(input("Enter instructor ID: "))
    cm.assign_instruct_to_course(course_code, instructor_id)
    print("Instructor assigned to course successfully")
    
def taking_attendance(cm):
    """
    Takes student attendance.
    """
    student_id = int(input("Enter student ID: "))
    status = input("Enter attendance status (If Present write P /If Absent write A): ")
    cm.take_attendance(student_id, status)
    print("Attendance recorded successfully")
    
def assigning_grades(cm):
    """
    Assigns grades to a student.
    """
    student_id = int(input("Enter student ID: "))
    course_code = input("Enter course code: ")
    grade_value = int(input("Enter grade (0-Pass, 1-Fail, 2-Incomplete): "))
    
    # Check if the grade value is valid
    if grade_value not in [0, 1, 2]:
        print("Invalid grade value. Please enter 0 for Pass, 1 for Fail, or 2 for Incomplete.")
        return
    
    grade = up.GradeStatusEnum(grade_value)
    result = cm.assign_std_grades(student_id, course_code, grade)
    
    # Check the result of assigning grades
    if isinstance(result, dict):
        print("Grade assigned successfully")
    else:
        print(result)

    
def get_std_info(cm):
    """
    Retrieves student information.
    """
    student_id = int(input("Enter student ID: "))
    student_info = cm.get_student_info(student_id)
    if student_info:
        print(student_info)
    else:
        print("Student not found")
        
def all_std_info(cm):
    """
    Retrieves all students' information.
    """
    all_students = cm.get_all_students_info()
    if all_students:
        for student_info in all_students:
            print(student_info)
            print("-" * 20)  # Separator between students
    else:
        print("No students found")
        
def all_attended_std(cm):
    """
    Retrieves all students who attended on a specific date.
    """
    date = input("Enter date (YYYY-MM-DD): ")
    attended_students = cm.get_all_attended_students(date)
    print(f"Date: {date}")
    if attended_students:
        for student in attended_students:
            print(f"Student ID: {student}")
    else:
        print("No students attended on this date")

def all_ins_info(cm):
    """
    Retrieves all instructors' information.
    """
    all_instructors = cm.get_all_instructors_info()
    if all_instructors:
        for inst_info in all_instructors:
            print(inst_info)
            print("-" * 20)  # Separator between students
    else:
        print("No instructors found") 
         
def all_course_info(cm):
    """
    Retrieves all students' information.
    """
    all_courses = cm.get_all_courses_info()
    if all_courses:
        for course_info in all_courses:
            print(course_info)
            print("-" * 20)  # Separator between courses
    else:
        print("No instructors found")  
                        
def all_grades(cm):
    """
    Retrieves all students' grades.
    """
    grades = cm.get_all_grades()
    if grades:
        for grades_info in grades:
            print("ID:Grades")
            print(grades_info)
            print("-" * 20)  # Separator between grades
    else:
        print("No grades found")
        
def display_menu():
    """
    Displays the main menu.
    """
    print("\nUniversity Course Management System")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Remove Student")
    print("4. Add Instructor")
    print("5. Update Instructor")
    print("6. Add Course")
    print("7. Change Course Status")
    print("8. Assign Instructor to Course")
    print("9. Take Attendance")
    print("10. Assign Grades")
    print("11. Get Student Information")
    print("12. Get All Students Information")
    print("13. Get All Attended Students")
    print("14. Get All Instructor")
    print("15. Get All Courses")
    print("16. Get All Grades of the Students")
    print("17. Exit")

def while_choice(choice, cm):
    """
    Handles user choices in the main menu loop.
    """
    while choice >= 1:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            adding_student(cm) 

        elif choice == 2:
            updating_student(cm)

        elif choice == 3:
            removing_student(cm)

        elif choice == 4:
            adding_instructor(cm)

        elif choice == 5:
            updating_instructor(cm)

        elif choice == 6:
            adding_course(cm)

        elif choice == 7:
            changing_course_status(cm)

        elif choice == 8:
            instructor_to_course(cm)

        elif choice == 9:
            taking_attendance(cm)

        elif choice == 10:
            assigning_grades(cm)

        elif choice == 11:
            get_std_info(cm)

        elif choice == 12:
            all_std_info(cm)

        elif choice == 13:
            all_attended_std(cm)
            
        elif choice == 14:
            all_ins_info(cm)
        
        elif choice == 15:
            all_course_info(cm)
            
        elif choice == 16:
            all_grades(cm)
        
        elif choice == 17:
            print("Exiting the program...")
            break

        else:
            print("Invalid choice, please try again.")

def main():
    cm = up.CourseManagement()
    choice = 1
    while_choice(choice, cm)
    
if __name__ == "__main__":
    main()