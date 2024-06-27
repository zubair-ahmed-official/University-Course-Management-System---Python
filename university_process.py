from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Tuple
from datetime import datetime

class GradeLevelEnum(Enum):
    FRESHMAN = 0
    SOPHOMORE = 1
    JUNIOR = 2
    SENIOR = 3

class CourseStatusEnum(Enum):
    ACTIVE = 0
    INACTIVE = 1
    UPCOMING = 2

class GradeStatusEnum(Enum):
    PASS = 0
    FAIL = 1
    INCOMPLETE = 2

@dataclass
class Student:
    std_id: int
    name: str
    grade: GradeLevelEnum
    address: str
    phone: str

@dataclass
class Course:
    course_code: str
    title: str
    credits: int
    instructor_id: int
    status: CourseStatusEnum = CourseStatusEnum.ACTIVE
    
@dataclass
class Instructor:
    instructor_id: int
    name: str
    subject: str
    email: str

class CourseManagement:
    def __init__(self):
        self.students: Dict[int, Student] = {}
        self.courses: Dict[str, Course] = {}
        self.instructors: Dict[int, Instructor] = {}
        self.attendance: Dict[int, Dict[str, str]] = {}
        self.grades: Dict[int, Dict[str, GradeStatusEnum]] = {}
        self.filename = "students.txt"
        self.last_student_id_file = "last_student_id.txt"
        self.instructors_id_file = "instructors_id.txt"
        self.students_id_file = "students_id.txt"
        self.load_student_ids()
        self.load_instructor_ids()
        self.load_courses()
        self.attendancefile = "attendance.txt" 

    def load_student_ids(self):
        """Load student IDs from file."""
        try:
            with open(self.students_id_file, 'r') as file:
                for line in file:
                    parts = line.strip().split(": ")
                    if len(parts) == 2:
                        student_id, student_name = int(parts[0]), parts[1]
                        self.students[student_id] = Student(student_id, student_name, "", "", "")
        except FileNotFoundError:
            pass  # If file not found, no need to load student IDs

    def save_student_ids(self):
        """Save student IDs to file."""
        with open(self.students_id_file, 'w') as file:
            for student_id, student in self.students.items():
                file.write(f"{student_id}: {student.name}\n")
    
    def add_student(self, name: str, grade: GradeLevelEnum, address: str, phone: str) -> Tuple[int, str]:
        """Add a new student to the database and append the info to the file."""
        new_id = max(self.students.keys(), default=0) + 1
        self.students[new_id] = Student(new_id, name, grade, address, phone)
        self.save_student_ids()  # Save updated student IDs to file

        with open("students.txt", 'a') as file:
            file.write(f"Student ID: {new_id}\n")
            file.write(f"Name: {name}\n")
            file.write(f"Grade: {grade.name}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Phone: {phone}\n")
            file.write("\n")
            file.write("\n")

        return new_id, "Student added successfully"

    def update_student(self, student_id: int, name: str, grade: GradeLevelEnum, address: str, phone: str) -> Tuple[int, str]:
        """Update an existing student's information and update the file."""
        if student_id in self.students:
            self.students[student_id] = Student(student_id, name, grade, address, phone)
            self.rewrite_students_file()
            return student_id, "Student updated successfully"
        else:
            return student_id, "Student not found"
        
    def remove_student(self, student_id: int):
        """Remove a student from the database."""
        if student_id in self.students:
            del self.students[student_id]
            # Update file after removing student info
            self.rewrite_all_students_file()
            
    def rewrite_students_file(self):
        """Rewrite the students file with updated information for a specific student."""
        with open("students.txt", 'r') as file:
            lines = file.readlines()

        with open("students.txt", 'w') as file:
            found_student = False
            for line in lines:
                if line.strip().startswith("Student ID:"):
                    student_id = int(line.split(": ")[1])
                    if student_id == self.students[student_id].std_id:
                        found_student = True 
                        file.write(f"Student ID: {self.students[student_id].std_id}\n")
                        file.write(f"Name: {self.students[student_id].name}\n")
                        file.write(f"Grade: {self.students[student_id].grade}\n")
                        file.write(f"Address: {self.students[student_id].address}\n")
                        file.write(f"Phone: {self.students[student_id].phone}\n")
                        file.write("\n")
          
    def get_student_info(self, student_id: int) -> str:
        """Retrieve student information by student ID from the file."""
        try:
            with open('students.txt', 'r') as file:
                students_data = file.readlines()
                student_info = ""
                found = False
                for line in students_data:
                    if line.startswith(f"Student ID: {student_id}"):
                        found = True
                    if found:
                        if line.strip() == "" and student_info:
                            break
                        student_info += line
                if student_info:
                    return student_info.strip()
                else:
                    return "Student not found"
        except FileNotFoundError:
            return "No student data file found."

    def get_all_students_info(self) -> List[str]:
        """Retrieve information of all students from the file in a formatted view."""
        all_students_info = []
        try:
            with open(self.filename, 'r') as file:
                students_data = file.readlines()
                student_info = ""
                for line in students_data:
                    if line.strip() == "":
                        if student_info:
                            all_students_info.append(student_info.strip())
                        student_info = ""
                    else:
                        student_info += line
                if student_info:
                    all_students_info.append(student_info.strip())
        except FileNotFoundError:
            print("No student data file found.")
        return all_students_info


    def rewrite_all_students_file(self):
        """Rewrite the file with all students' information."""
        with open("students.txt", 'w') as file:
            for student in self.students.values():
                file.write(f"Student ID: {student.std_id}\n")
                file.write(f"Name: {student.name}\n")
                file.write(f"Grade: {student.grade}\n")
                file.write(f"Address: {student.address}\n")
                file.write(f"Phone: {student.phone}\n")
                file.write("\n")

    def load_instructor_ids(self):
        """Load instructor IDs from file."""
        try:
            with open(self.instructors_id_file, 'r') as file:
                for line in file:
                    parts = line.strip().split(": ")
                    if len(parts) == 2:
                        instructor_id, instructor_name = int(parts[0]), parts[1]
                        self.instructors[instructor_id] = Instructor(instructor_id, instructor_name, "", "")
        except FileNotFoundError:
            pass  # If file not found, no need to load instructor IDs

    def save_instructor_ids(self):
        """Save instructor IDs to file."""
        with open(self.instructors_id_file, 'w') as file:
            for instructor_id, instructor in self.instructors.items():
                file.write(f"{instructor_id}: {instructor.name}\n")
                
    def add_instructor(self, name: str, subject: str, email: str) -> Tuple[int, str]:
        """Add a new instructor to the database and append the info to the file."""
        new_id = max(self.instructors.keys(), default=0) + 1
        self.instructors[new_id] = Instructor(new_id, name, subject, email)
        self.save_instructor_ids()  # Save updated instructor IDs to file
        
        with open("instructors.txt", 'a') as file:
            file.write(f"Instructor ID: {new_id}\n")
            file.write(f"Name: {name}\n")
            file.write(f"Subject: {subject}\n")
            file.write(f"Email: {email}\n")
            file.write("\n")
        
        return new_id, "Instructor added successfully"

    def update_instructor(self, instructor_id: int, name: str, subject: str, email: str) -> Tuple[int, str]:
        """Update an existing instructor’s information and update the file."""
        if instructor_id in self.instructors:
            self.instructors[instructor_id] = Instructor(instructor_id, name, subject, email)
            self.rewrite_instructors_file()
            return instructor_id, "Instructor updated successfully"
        else:
            return instructor_id, "Instructor not found"
        
    def get_all_instructors_info(self) -> List[str]:
        """Retrieve information of all instructors from the file in a formatted view."""
        all_instructors_info = []
        try:
            with open("instructors.txt", 'r') as file:
                instructors_data = file.readlines()
                instructor_info = ""
                for line in instructors_data:
                    if line.strip() == "":
                        if instructor_info:
                            all_instructors_info.append(instructor_info.strip())
                        instructor_info = ""
                    else:
                        instructor_info += line
                if instructor_info:
                    all_instructors_info.append(instructor_info.strip())
        except FileNotFoundError:
            print("No instructor data file found.")
        return all_instructors_info
       
    def add_course(self, course_code: str, title: str, credits: int, instructor_id: int, status: str)-> Tuple[str, str]:
        """Add a new course to the database and update the file."""
        if course_code in self.courses:
            return course_code, "Course code already exists"

        # Check if the instructor ID exists
        if instructor_id not in self.instructors:
            return course_code, "Instructor ID not found"

        # Create a new course instance and add it to the courses dictionary
        new_course = Course(course_code, title, credits, instructor_id, status)
        self.courses[course_code] = new_course

        # Update the file with the new course information
        self.update_courses_file(new_course)

        return course_code, "Course added successfully"

    def update_courses_file(self, course: Course):
        """Update the file with the new course information."""
        try:
            with open("all_courses.txt", 'a') as file:
                file.write(f"Course Code: {course.course_code}\n")
                file.write(f"Title: {course.title}\n")
                file.write(f"Credits: {course.credits}\n")
                file.write(f"Instructor ID: {course.instructor_id}\n")
                file.write(f"Status: {course.status}\n")
                file.write("\n")
            print("Course information written to file successfully.")
        except Exception as e:
            print(f"Error writing course information to file: {e}")

    def get_all_courses_info(self) -> List[str]:
        """Retrieve information of all courses from the file in a formatted view."""
        all_courses_info = []
        try:
            with open("all_courses.txt", 'r') as file:
                courses_data = file.readlines()
                course_info = ""
                for line in courses_data:
                    if line.strip() == "":
                        if course_info:
                            all_courses_info.append(course_info.strip())
                        course_info = ""
                    else:
                        course_info += line
                if course_info:
                    all_courses_info.append(course_info.strip())
        except FileNotFoundError:
            print("No courses data file found.")
        return all_courses_info

    # def change_course_status(self, course_code: str, status: CourseStatusEnum) -> int:
    def load_courses(self):
        """Load courses from file."""
        try:
            with open('all_courses.txt', 'r') as file:
                while True:
                    line = file.readline()
                    if not line:
                        break
                    course_code = line.strip().split(": ")[1]
                    title = file.readline().strip().split(": ")[1]
                    credits = int(file.readline().strip().split(": ")[1])
                    instructor_id = int(file.readline().strip().split(": ")[1])
                    status = CourseStatusEnum[file.readline().strip().split(": ")[1]]
                    self.courses[course_code] = Course(course_code, title, credits, instructor_id, status)
                    file.readline()  # skip the empty line
        except FileNotFoundError:
            pass  # If file not found, no need to load courses

    def save_courses(self):
        """Save all courses to the file."""
        with open('all_courses.txt', 'w') as file:
            for course in self.courses.values():
                file.write(f"Course Code: {course.course_code}\n")
                file.write(f"Title: {course.title}\n")
                file.write(f"Credits: {course.credits}\n")
                file.write(f"Instructor ID: {course.instructor_id}\n")
                file.write(f"Status: {course.status.name}\n")
                file.write("\n")

    def change_course_status(self, course_code: str, new_status: CourseStatusEnum) -> str:
        """Change the status of a course and update the file."""
        if course_code in self.courses:
            self.courses[course_code].status = new_status
            self.save_courses()
            return f"Course status updated successfully for {course_code} to {new_status.name}"
        else:
            return "Course not found"
    

    def assign_instruct_to_course(self, course_code: str, instructor_id: int):
        """Assign an instructor to teach a specific course and update the file."""
        if course_code in self.courses and instructor_id in self.instructors:
            self.courses[course_code].instructor_id = instructor_id
            self.rewrite_courses_file()  # Update course file

    def take_attendance(self, student_id: int, status: str) -> Dict[int, Dict[str, str]]:
        """Record attendance for a student for today and update the file."""
        today = datetime.today().strftime('%Y-%m-%d')
        if student_id not in self.attendance:
            self.attendance[student_id] = {}
        self.attendance[student_id][today] = status
        self.rewrite_attendance_file()  # Update attendance file
        return self.attendance
    
    def get_all_attended_students(self, date: str) -> List[int]:
        """
        Retrieve all students who have attended on a specific date.
        """
        attended_students = []

        for student_id, dates in self.attendance.items():
            if date in dates and dates[date] == "P":  # Assuming 'P' is the status indicating attendance
                attended_students.append(student_id)

        return attended_students
    
    def assign_std_grades(self, student_id: int, course_code: str, grade: GradeStatusEnum) -> Dict[int, Dict[str, GradeStatusEnum]]:
            """Assign a grade to a student for a specific course and update the file."""
            student_info = self.get_student_info(student_id)
            if student_info != "Student not found":
                if student_id not in self.grades:
                    self.grades[student_id] = {}
                self.grades[student_id][course_code] = grade
                self.rewrite_grades_file()  # Update grades file
                return self.grades
            else:
                return "Student not found"

    def get_all_grades(self) -> List[str]:
        """Retrieve information of all courses from the file in a formatted view."""
        all_grades_info = []
        try:
            with open("grades.txt", 'r') as file:
                grades_data = file.readlines()
                grades_info = ""
                for line in grades_data:
                    if line.strip() == "":
                        if grades_info:
                            all_grades_info.append(grades_info.strip())
                        grades_info = ""
                    else:
                        grades_info += line
                if grades_info:
                    all_grades_info.append(grades_info.strip())
        except FileNotFoundError:
            print("No grades file found.")
        return all_grades_info

    # Helper methods for file operations
    def rewrite_instructors_file(self):
        """Rewrite the instructors file with updated information."""
        with open("instructors.txt", 'w') as file:
            for instructor in self.instructors.values():
                file.write(f"Instructor ID: {instructor.instructor_id}\n")
                file.write(f"Name: {instructor.name}\n")
                file.write(f"Subject: {instructor.subject}\n")
                file.write(f"Email: {instructor.email}\n")
                file.write("\n")

    def rewrite_courses_file(self):
        """Rewrite the courses file with updated information."""
        with open("all_courses.txt", 'w') as file:
            for course in self.courses.values():
                file.write(f"Course Code: {course.course_code}\n")
                file.write(f"Title: {course.title}\n")
                file.write(f"Credits: {course.credits}\n")
                file.write(f"Instructor ID: {course.instructor_id}\n")
                file.write(f"Status: {course.status.name}\n")
                file.write("\n")

    def rewrite_attendance_file(self):
        """Rewrite the attendance file with updated information."""
        with open("attendance.txt", 'w') as file:
            for student_id, dates in self.attendance.items():
                file.write(f"Student ID: {student_id}\n")
                for date, status in dates.items():
                    file.write(f"{date}: {status}\n")
                file.write("\n")

    def rewrite_grades_file(self):
        """Rewrite the grades file with updated information."""
        with open("grades.txt", 'w') as file:
            for student_id, course_grades in self.grades.items():
                file.write(f"Student ID: {student_id}\n")
                for course_code, grade in course_grades.items():
                    file.write(f"Course Code: {course_code}\n")
                    file.write(f"Grade: {grade.name}\n")
                file.write("\n")