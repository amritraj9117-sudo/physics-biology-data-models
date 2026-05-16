import datetime
from dateutil import parser

class Person(object):
    def __init__(self, name):
        """Assumes name is a string. Creates a person."""
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank+1:]
        except ValueError:
            self._last_name = name
        self._birthday = None
        
    def get_name(self):
        """Returns self's full name"""
        return self._name
    
    def get_last_name(self):
        """Returns person's last name"""
        return self._last_name
    
    def set_birthday(self, birthdate):
        """Sets birthday. Accepts datetime.date, datetime.datetime, or string."""
        if isinstance(birthdate, datetime.datetime):
            # normalize datetime.datetime to date
            self._birthday = birthdate.date()
        elif isinstance(birthdate, str):
            # parse string into datetime.date
            self._birthday = parser.parse(birthdate).date()
        elif isinstance(birthdate, datetime.date):
            self._birthday = birthdate
        else:
            raise TypeError("birthdate must be datetime.date, datetime.datetime, or a date string")
            
    def get_age(self):
        """Returns self's current age in days"""
        if self._birthday is None:
            raise ValueError("Birthday has not been set.")
        return (datetime.date.today() - self._birthday).days
    
    def __lt__(self, other):
        """Returns True if self's name is lexicographically
           less than other's name, and False otherwise"""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name
    
    def __str__(self):
        """Returns self's name"""
        return self._name


class Politician(Person):
    """Politician is a Person who belongs to a political party"""
    def __init__(self, name):
        super().__init__(name)
        self._party = None
        
    def set_party(self, party_name):
        self._party = party_name
        
    def get_party(self):
        return self._party


class Course(object):
    def __init__(self, course_code, course_title):
        """code and title are strings"""
        self.code = course_code
        self.title = course_title
        self._students = []
        
    def add_student(self, student):
        if student not in self._students:
            self._students.append(student)
            
    def get_students(self):
        for stud in self._students:
            yield stud
            
    def __str__(self):
        return f"{self.code}:{self.title}"


class IISER_person(Person):
    _next_id_num = 0 # Class variable
    
    def __init__(self, name):
        super().__init__(name)
        self._id_num = IISER_person._next_id_num
        IISER_person._next_id_num += 1
        
    def get_id_num(self):
        return self._id_num
    
    def __lt__(self, other):
        """Returns True if self's ID number is less than
           other's ID number, and False otherwise"""
        return self._id_num < other._id_num
        

class Student(IISER_person):
    def __init__(self, name):
        super().__init__(name)
        self._courses = []

    def enroll(self, course):
        """Takes course object as an argument and links both ways"""
        if isinstance(course, Course):
            if course not in self._courses:
                self._courses.append(course)
                course.add_student(self) # FIXED: This updates the course roster too!

    def get_courses(self):
        return self._courses


class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self._year = class_year
        
    def get_class(self):
        return self._year
        

class Grad(Student):
    pass


# --- Test Code ---

# Create Students
s1 = UG('Billy Beaver', 1984)
s2 = Grad('Buzz Aldrin')
s3 = UG('Jane Doe', 2023)

# Create Courses
c1 = Course('101', 'Introduction to Programming')
c2 = Course('201', 'Calculus')

# Enroll Students
s1.enroll(c1)
s1.enroll(c2)
s2.enroll(c1)

# Print Course Rosters
print("--- Course Rosters ---")
for course in [c1, c2]:
    print(f"\n{course}") # This tests your Course __str__
    for student in course.get_students():
        print(f"  {student.get_name()} ({student.get_id_num()})")

# Print Student Schedules
print("\n--- Student Schedules ---")
for student in [s1, s2, s3]:
    print(f"\n{student.get_name()}'s Schedule:")
    courses = student.get_courses()
    if not courses:
        print("  Not enrolled in any courses.")
    for course in courses:
        print(f"  {course}") # This also tests your Course __str__