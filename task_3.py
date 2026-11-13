class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surename = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}   

    def average_grades(self):
        count_grades = 0
        sum_grades = 0
        for grades in self.grades.values():
            count_grades += len(grades)
            sum_grades += sum(grades)
        if count_grades == 0:
            return 'Оценок нет'
        else:
            return sum_grades / count_grades

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surename}\n'
                f'Средняя оценка за лекции: {self.average_grades()}\n')

    def __gt__(self, other):
        return self.average_grades() > other.average_grades()


class Reviewer(Mentor):
    def rate_students(self, student, course, grade):
        if not isinstance(student, Student) \
            or course not in self.courses_attached \
            or (course not in student.courses_in_progress and course not in student.finished_courses):
            return 'Ошибка'
        student.grades.setdefault(course, []).append(grade)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surename}\n')


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surename = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []        
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer) \
            or course not in lecturer.courses_attached \
            or (course not in self.courses_in_progress and course not in self.finished_courses):
            return 'Ошибка'
        lecturer.grades.setdefault(course, []).append(grade)

    def average_grades(self):
        count_grades = 0
        sum_grades = 0
        for grades in self.grades.values():
            count_grades += len(grades)
            sum_grades += sum(grades)
        if count_grades == 0:
            return 'Оценок нет'
        else:
            return sum_grades / count_grades
    
    def __str__(self):               
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surename}\n'
                f'Средняя оценка за домашние задания: {self.average_grades()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def __gt__(self, other):
        return self.average_grades() > other.average_grades()


some_student = Student('Ruoy', 'Eman', 'm')
some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')

some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
some_lecturer.courses_attached += ['Python', 'Git', 'Введение в программирование']
some_reviewer.courses_attached += ['Python', 'Git', 'Введение в программирование']


some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Git', 9)
some_student.rate_lecture(some_lecturer, 'Git', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Git', 10)
some_student.rate_lecture(some_lecturer, 'Git', 10)


some_reviewer.rate_students(some_student, 'Python', 10)
some_reviewer.rate_students(some_student, 'Python', 10)
some_reviewer.rate_students(some_student, 'Git', 10)
some_reviewer.rate_students(some_student, 'Введение в программирование', 10)
some_reviewer.rate_students(some_student, 'Введение в программирование', 10)
some_reviewer.rate_students(some_student, 'Python', 10)
some_reviewer.rate_students(some_student, 'Python', 9)
some_reviewer.rate_students(some_student, 'Git', 10)
some_reviewer.rate_students(some_student, 'Введение в программирование', 10)
some_reviewer.rate_students(some_student, 'Введение в программирование', 10)

print(some_reviewer)
print(some_lecturer)
print(some_student)

other_student = Student('Tom', 'Neman', 'm')
other_lecturer = Lecturer('Sam', 'Buggy')

other_student.grades = {'Python': [10, 10, 10, 10, 10], 'Git': [5, 7, 6, 10]}
other_lecturer.grades = {'Python': [10, 10, 10, 10, 10], 'Git': [10, 10], 'Введение в программирование': [10, 10, 10, 10]}

print(some_student > other_student)
print(some_lecturer > other_lecturer)







