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
            return 0
        else:
            return sum_grades / count_grades

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surename}\n'
                f'Средняя оценка за лекции: {self.average_grades():.2f}')

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
                f'Фамилия: {self.surename}')


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
            return 0
        else:
            return sum_grades / count_grades
    
    def __str__(self):               
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surename}\n'
                f'Средняя оценка за домашние задания: {self.average_grades():.2f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __gt__(self, other):
        return self.average_grades() > other.average_grades()

def average_grade_students(course, students_lst):
    average_grade_s = 0
    count_grade_s = 0
    if not students_lst:
        return 'Список студентов пуст'
    for student in students_lst:
        if course in student.grades:
            average_grade_s += sum(student.grades[course])
            count_grade_s += len(student.grades[course]) 
    if count_grade_s != 0:
        return f'Cредняя оценка за домашние задания студентов на курсе {course}: {average_grade_s / count_grade_s:.2f}'
    else:
        return f'На курсе {course} у студентов нет оценок'

def average_grade_lecturers(course, lecturers_lst):
    average_grade_s = 0
    count_grade_s = 0
    if not lecturers_lst:
        return 'Список лекторов пуст'
    for lecturer in lecturers_lst:
        if course in lecturer.grades:
            average_grade_s += sum(lecturer.grades[course])
            count_grade_s += len(lecturer.grades[course]) 
    if count_grade_s != 0:
        return f'Средняя оценка за лекции всех лекторов на курсе {course}: {average_grade_s / count_grade_s:.2f}'
    else:
        return f'На курсе {course} лекторам оценки не ставили'


student1 = Student('Иван', 'Иванов', 'м')
student2 = Student('Ольга', 'Ольгина', 'ж')

reviewer1 = Reviewer('Петр', 'Петров')
reviewer2 = Reviewer('Антон', 'Антонов')

lecturer1 = Lecturer('Василий', 'Васильев')
lecturer2 = Lecturer('Григорий', 'Григорьев')

student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student1.courses_in_progress += ['ООП']

student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Введение в программирование']

lecturer1.courses_attached += ['Python', 'Git', 'Введение в программирование']
lecturer2.courses_attached += ['Python', 'Git', 'Введение в программирование']

reviewer1.courses_attached += ['Python', 'Git', 'Введение в программирование']
reviewer2.courses_attached += ['Python', 'Git']


student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer2, 'Введение в программирование', 10)

student2.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer2, 'Git', 10)
student2.rate_lecture(lecturer2, 'Python', 6)


reviewer1.rate_students(student1, 'Python', 10)
reviewer1.rate_students(student1, 'Python', 10)
reviewer1.rate_students(student2, 'Git', 10)
reviewer2.rate_students(student2, 'Введение в программирование', 10)
reviewer2.rate_students(student2, 'Введение в программирование', 10)
reviewer2.rate_students(student1, 'Python', 9)

print(reviewer1)
print(reviewer2)
print()
print(lecturer1)
print(lecturer2)
print()
print(student1)
print(student2)
print()
print(student1 > student2)
print(lecturer1 > lecturer2)

students_lst = [student1, student2]
lecturers_lst = [lecturer1, lecturer2]

print(average_grade_students('Python', students_lst))
print(average_grade_lecturers('Python', lecturers_lst))
print(average_grade_students('Git', students_lst))
print(average_grade_lecturers('Git', lecturers_lst))
print(average_grade_students('ООП', students_lst))
print(average_grade_lecturers('ООП', lecturers_lst))







