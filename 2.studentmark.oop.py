# --- Base Classes ---

class Student:
    """Represents a student with basic information."""
    
    def __init__(self, student_id, name, dob):
        # Encapsulation: Attributes are set during initialization
        self._student_id = student_id
        self._name = name
        self._dob = dob

    # Properties for controlled access (Encapsulation)
    @property
    def student_id(self):
        return self._student_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def dob(self):
        return self._dob

    # Polymorphic method: input is handled by the manager, but this defines the string representation
    def __str__(self):
        return f"{self.student_id:<10} {self.name:<25} {self.dob:<10}"

class Course:
    """Represents a course."""
    
    def __init__(self, course_id, name):
        # Encapsulation
        self._course_id = course_id
        self._name = name

    # Properties for controlled access
    @property
    def course_id(self):
        return self._course_id
    
    @property
    def name(self):
        return self._name

    # Polymorphic method
    def __str__(self):
        return f"{self.course_id:<10} {self.name:<30}"

# --- Manager Class ---

class MarkManager:
    """Manages all students, courses, and marks, centralizing operations."""
    
    def __init__(self):
        self._students = []  # List of Student objects
        self._courses = []   # List of Course objects
        # Marks stored as: {student_id: {course_id: mark_value, ...}}
        self._marks = {}     

    # --- Helper Methods ---

    def _get_int_input(self, prompt):
        """Safely handles integer input."""
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def _get_mark_input(self, prompt):
        """Safely handles mark input (float between 0 and 20)."""
        while True:
            try:
                mark_value = float(input(prompt))
                if 0 <= mark_value <= 20:
                    return mark_value
                else:
                    print("Mark must be between 0 and 20.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def _find_student(self, student_id):
        """Finds a Student object by ID."""
        for student in self._students:
            if student.student_id == student_id:
                return student
        return None

    def _find_course(self, course_id):
        """Finds a Course object by ID."""
        for course in self._courses:
            if course.course_id == course_id:
                return course
        return None

    # --- Input Methods (Polymorphism: using .input() methods) ---

    def input_students(self):
        """Input number of students and their details."""
        number_of_students = self._get_int_input("Enter the number of students in the class: ")
        
        for i in range(number_of_students):
            print(f"\n--- Student {i + 1} ---")
            student_identifier = input("Enter student ID: ")
            
            if self._find_student(student_identifier):
                print("Student ID already exists. Skipping this student.")
                continue
                
            full_name = input("Enter student full name: ")
            date_of_birth = input("Enter student DoB (e.g., DD/MM/YYYY): ")
            
            # Create a new Student object
            new_student = Student(student_identifier, full_name, date_of_birth)
            self._students.append(new_student)
            
            # Initialize mark entry
            self._marks[student_identifier] = {}
            
        print(f"\nSuccessfully added {len(self._students)} student(s).")

    def input_courses(self):
        """Input number of courses and their details."""
        number_of_courses = self._get_int_input("Enter the number of courses: ")
        
        for i in range(number_of_courses):
            print(f"\n--- Course {i + 1} ---")
            course_identifier = input("Enter course ID: ")
            
            if self._find_course(course_identifier):
                print("Course ID already exists. Skipping this course.")
                continue
                
            course_name = input("Enter course name: ")
            
            # Create a new Course object
            new_course = Course(course_identifier, course_name)
            self._courses.append(new_course)
            
        print(f"\nSuccessfully added {len(self._courses)} course(s).")

    def input_marks_for_course(self):
        """Select a course and input marks for all students in that course."""
        if not self._courses:
            print("No courses have been added yet. Please add a course first.")
            return
        if not self._students:
            print("No students have been added yet. Please add students first.")
            return

        self.list_courses()
        course_identifier = input("\nSelect a Course ID to input marks: ")
        selected_course = self._find_course(course_identifier)
        
        if not selected_course:
            print("Course not found.")
            return
        
        print(f"\n--- Input Marks for {selected_course.name} ---")
        
        for student in self._students:
            prompt = f"Enter mark for {student.name} (ID: {student.student_id}) in {selected_course.name} [0-20]: "
            mark_value = self._get_mark_input(prompt)
            
            # Use student_id and course_id properties to store mark
            self._marks[student.student_id][selected_course.course_id] = mark_value
            
        print("\nMarks successfully recorded for the selected course.")

    # --- Listing Methods (Polymorphism: using .list() methods) ---

    def list_students(self):
        """List all students (id, name, DoB)."""
        if not self._students:
            print("No students to list.")
            return
            
        print("\n## Student List")
        print("-" * 45)
        print(f"{'ID':<10} {'Full Name':<25} {'DoB':<10}")
        print("-" * 45)
        
        # Polymorphism in action: calling __str__ implicitly on each Student object
        for student in self._students:
            print(student)
            
        print("-" * 45)

    def list_courses(self):
        """List all courses (id, name)."""
        if not self._courses:
            print("No courses to list.")
            return
            
        print("\n## Course List")
        print("-" * 40)
        print(f"{'ID':<10} {'Course Name':<30}")
        print("-" * 40)
        
        # Polymorphism in action: calling __str__ implicitly on each Course object
        for course in self._courses:
            print(course)
            
        print("-" * 40)

    def show_student_marks_for_course(self):
        """Shows all student marks for a given course."""
        if not self._courses or not self._students:
            print("Must have courses and students to show marks.")
            return

        self.list_courses()
        course_identifier = input("\nEnter the Course ID to display student marks: ")
        selected_course = self._find_course(course_identifier)
        
        if not selected_course:
            print("Course not found.")
            return

        course_name = selected_course.name
        course_id = selected_course.course_id
        
        print(f"\n## Marks for Course: {course_name}")
        print("-" * 50)
        print(f"{'Student ID':<15} {'Student Name':<20} {'Mark':<10}")
        print("-" * 50)

        for student in self._students:
            student_id = student.student_id
            full_name = student.name
            
            # Access mark using the encapsulated structure
            mark_value = self._marks.get(student_id, {}).get(course_id, "N/A")
            
            if isinstance(mark_value, float):
                mark_str = f"{mark_value:.2f}"
            else:
                mark_str = mark_value
                
            print(f"{student_id:<15} {full_name:<20} {mark_str:<10}")
        print("-" * 50)

# --- Main Program Loop ---

def main():
    """The main function to run the OOP student mark management system."""
    
    manager = MarkManager() # Instantiate the manager class
    
    menu_options = {
        '1': ("Input students", manager.input_students),
        '2': ("Input courses", manager.input_courses),
        '3': ("Input marks for a course", manager.input_marks_for_course),
        '4': ("List students", manager.list_students),
        '5': ("List courses", manager.list_courses),
        '6': ("Show student marks for a given course", manager.show_student_marks_for_course),
        '0': ("Exit", None)
    }

    while True:
        print("\n" + "="*50)
        print("OOP Student Mark Management System")
        print("="*50)
        for key, (description, _) in menu_options.items():
            print(f"[{key}] {description}")
        print("-" * 50)
        
        choice_input = input("Enter your choice: ")
        
        if choice_input == '0':
            print("\nExiting the program.!")
            break
        
        if choice_input in menu_options:
            menu_options[choice_input][1]() 
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()