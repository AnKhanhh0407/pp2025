

class Student:
    def __init__(self, sid, name, dob):
        self._id = sid
        self._name = name
        self._dob = dob

    def input(self):
        self._id = input("Student ID: ")
        self._name = input("Student Name: ")
        self._dob = input("Student DOB: ")

    def __str__(self):
        return f"{self._id} - {self._name} - {self._dob}"

    def get_id(self):
        return self._id


class Course:
    def __init__(self, cid, name):
        self._id = cid
        self._name = name

    def input(self):
        self._id = input("Course ID: ")
        self._name = input("Course Name: ")

    def __str__(self):
        return f"{self._id} - {self._name}"

    def get_id(self):
        return self._id


class Mark:
    def __init__(self, student_id, course_id, mark):
        self._student_id = student_id
        self._course_id = course_id
        self._mark = mark

    def __str__(self):
        return f"Student {self._student_id} in course {self._course_id}: {self._mark}"

    def get_student(self):
        return self._student_id

    def get_course(self):
        return self._course_id


class MarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_student(self):
        s = Student("", "", "")
        s.input()
        self.students.append(s)

    def input_course(self):
        c = Course("", "")
        c.input()
        self.courses.append(c)

    def input_mark(self):
        sid = input("Student ID: ")
        cid = input("Course ID: ")
        mark = float(input("Mark: "))
        self.marks.append(Mark(sid, cid, mark))

    def list_students(self):
        for s in self.students:
            print(s)

    def list_courses(self):
        for c in self.courses:
            print(c)

    def list_marks(self):
        for m in self.marks:
            print(m)

    def list(self, item_type):
        if item_type == "student":
            self.list_students()
        elif item_type == "course":
            self.list_courses()
        elif item_type == "mark":
            self.list_marks()


m = MarkManagement()

while True:
    print("\n===== MENU =====")
    print("1. Add student")
    print("2. Add course")
    print("3. Add mark")
    print("4. List students")
    print("5. List courses")
    print("6. List marks")
    print("0. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        m.input_student()
    elif choice == "2":
        m.input_course()
    elif choice == "3":
        m.input_mark()
    elif choice == "4":
        m.list("student")
    elif choice == "5":
        m.list("course")
    elif choice == "6":
        m.list("mark")
    elif choice == "0":
        break
