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



