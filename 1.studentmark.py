students = []
courses = []
marks = {}

def get_int_input(prompt):
    while True:
        try:
            number_input = input(prompt)
            return int(number_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_mark_input(prompt):
    while True:
        try:
            mark_value = float(input(prompt))
            if 0 <= mark_value <= 20:
                return mark_value
            else:
                print("Mark must be between 0 and 20.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def find_item_by_id(item_list, item_identifier):
    for item in item_list:
        if item[0] == item_identifier:
            return item
    return None

def input_students():
    number_of_students = get_int_input("Enter the number of students in the class: ")
    
    for i in range(number_of_students):
        print(f"\n--- Student {i + 1} ---")
        student_identifier = input("Enter student ID: ")
        
        if find_item_by_id(students, student_identifier):
            print("Student ID already exists. Skipping this student.")
            continue
            
        full_name = input("Enter student full name: ")
        date_of_birth = input("Enter student DoB (e.g., DD/MM/YYYY): ")
        
        students.append((student_identifier, full_name, date_of_birth))
        marks[student_identifier] = {}
        
    print(f"\nSuccessfully added {len(students)} student(s).")

def input_courses():
    number_of_courses = get_int_input("Enter the number of courses: ")
    
    for i in range(number_of_courses):
        print(f"\n--- Course {i + 1} ---")
        course_identifier = input("Enter course ID: ")
        
        if find_item_by_id(courses, course_identifier):
            print("Course ID already exists. Skipping this course.")
            continue
            
        course_name = input("Enter course name: ")
        
        courses.append((course_identifier, course_name))
        
    print(f"\nSuccessfully added {len(courses)} course(s).")

def input_marks_for_course():
    if not courses:
        print("No courses have been added yet. Please add a course first.")
        return
    if not students:
        print("No students have been added yet. Please add students first.")
        return

    list_courses()
    course_identifier = input("\nSelect a Course ID to input marks: ")
    selected_course = find_item_by_id(courses, course_identifier)
    
    if not selected_course:
        print("Course not found.")
        return
    
    print(f"\n--- Input Marks for {selected_course[1]} ---")
    
    for student_identifier, full_name, _ in students:
        prompt = f"Enter mark for {full_name} (ID: {student_identifier}) in {selected_course[1]} [0-20]: "
        mark_value = get_mark_input(prompt)
        
        marks[student_identifier][course_identifier] = mark_value
        
    print("\nMarks successfully recorded for the selected course.")

def list_students():
    if not students:
        print("No students to list.")
        return
        
    print("\n## Student List")
    print("-" * 45)
    print(f"{'ID':<10} {'Full Name':<25} {'DoB':<10}")
    print("-" * 45)
    for student_identifier, full_name, date_of_birth in students:
        print(f"{student_identifier:<10} {full_name:<25} {date_of_birth:<10}")
    print("-" * 45)

def list_courses():
    if not courses:
        print("No courses to list.")
        return
        
    print("\n## Course List")
    print("-" * 40)
    print(f"{'ID':<10} {'Course Name':<30}")
    print("-" * 40)
    for course_identifier, course_name in courses:
        print(f"{course_identifier:<10} {course_name:<30}")
    print("-" * 40)

def show_student_marks_for_course():
    if not courses or not students:
        print("Must have courses and students to show marks.")
        return

    list_courses()
    course_identifier = input("\nEnter the Course ID to display student marks: ")
    selected_course = find_item_by_id(courses, course_identifier)
    
    if not selected_course:
        print("Course not found.")
        return

    course_name = selected_course[1]
    
    print(f"\n## Marks for Course: {course_name}")
    print("-" * 50)
    print(f"{'Student ID':<15} {'Student Name':<20} {'Mark':<10}")
    print("-" * 50)

    for student_identifier, full_name, _ in students:
        mark_value = marks.get(student_identifier, {}).get(course_identifier, "N/A")
        
        if isinstance(mark_value, float):
            mark_str = f"{mark_value:.2f}"
        else:
            mark_str = mark_value
            
        print(f"{student_identifier:<15} {full_name:<20} {mark_str:<10}")
    print("-" * 50)

def main():
    menu_options = {
        '1': ("Input students", input_students),
        '2': ("Input courses", input_courses),
        '3': ("Input marks for a course", input_marks_for_course),
        '4': ("List students", list_students),
        '5': ("List courses", list_courses),
        '6': ("Show student marks for a given course", show_student_marks_for_course),
        '0': ("Exit", None)
    }

    while True:
        print("\n" + "="*50)
        print("Student Mark Management System")
        print("="*50)
        for key, (description, _) in menu_options.items():
            print(f"[{key}] {description}")
        print("-" * 50)
        
        choice_input = input("Enter your choice: ")
        
        if choice_input == '0':
            print("\nExiting the program. Goodbye!")
            break
        
        if choice_input in menu_options:
            menu_options[choice_input][1]() 
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()