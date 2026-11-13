class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surename = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}   


class Reviewer(Mentor):
    
    def rate_students(self, student, course, grade):
        if not isinstance(student, Student) \
            or course not in self.courses_attached \
            or course not in student.courses_in_progress:
            return 'Ошибка'
        student.grades.setdefault(course, []).append(grade)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surename = surname
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer) \
            or course not in lecturer.courses_attached \
            or course not in self.courses_in_progress:
            return 'Ошибка'
        lecturer.grades.setdefault(course, []).append(grade)


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')
 
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
 
print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка
 
print(lecturer.grades)  # {'Python': [7]}

