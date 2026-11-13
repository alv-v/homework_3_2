'''
Задание № 1. Наследование

Исходя из квиза к предыдущему занятию, 
у нас уже есть класс преподавателей и класс студентов (вы можете взять этот код за основу или написать свой). 
Студентов пока оставим без изменения, а вот преподаватели бывают разные, 
поэтому теперь класс Mentor должен стать родительским классом,
а от него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания).
Очевидно, имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса. 
А чем же будут специфичны дочерние классы? Об этом в следующих заданиях. 
А пока можете проверить, что успешно реализовали дочерние классы

'''

class Mentor:
    def __init__(self, name, surename):
        self.name = name
        self.surename = surename
        self.courses_attached = []


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    pass


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []



