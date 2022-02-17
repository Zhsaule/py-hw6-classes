# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Домашнее задание к лекции «Объекты и классы. Инкапсуляция, наследование и полиморфизм»
def avg_course_grades(some_list, some_course=None):
    grades_if_list = [list_if for dict_in in some_list
                      for dict_if in dict_in.grades.items() if (dict_if[0] == some_course or some_course is None)
                      for list_if in dict_if[1]]
    if len(grades_if_list) != 0:
        grades_if = sum(grades_if_list) / len(grades_if_list)
    else:
        grades_if = 0
    return grades_if


list_student = []
list_lecturer = []
list_reviewer = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        list_student.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
                course in self.courses_in_progress + self.finished_courses \
                and 0 < grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {avg_course_grades([self]):.2f} \n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    #     добавим возможность сравнения Student
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение не корректно, сравниваемый не является студентом')
            return ' '
        return avg_course_grades([self]) < avg_course_grades([other])


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        list_lecturer.append(self)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {avg_course_grades([self]):.2f}\n'
        return res

    #     добавим возможность сравнения Lecturer
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение не корректно, сравниваемый не является лектором.')
            return ''
        return avg_course_grades([self]) < avg_course_grades([other])


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []
        list_reviewer.append(self)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress and 0 < grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Проверяемые курсы: {", ".join(self.courses_attached)}\n'
        return res


first_lecturer = Lecturer('First', 'Lecturer')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Вводный курс']

second_lecturer = Lecturer('Second', 'Lecturer')
second_lecturer.courses_attached += ['Git']
second_lecturer.courses_attached += ['Java']

first_student = Student('First', 'Student', 'your_gender')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
first_student.courses_in_progress += ['Java']
first_student.finished_courses += ['Вводный курс']
first_student.rate_lecturer(first_lecturer, 'Python', 9)
first_student.rate_lecturer(first_lecturer, 'Git', 10)
first_student.rate_lecturer(first_lecturer, 'Вводный курс', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 8)
first_student.rate_lecturer(first_lecturer, 'Вводный курс', 10)
first_student.rate_lecturer(second_lecturer, 'Git', 9)
first_student.rate_lecturer(second_lecturer, 'Java', 8)

second_student = Student('Second', 'Student', 'your_gender')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Вводный курс']
second_student.rate_lecturer(second_lecturer, 'Git', 8)
second_student.rate_lecturer(second_lecturer, 'Java', 7)
second_student.rate_lecturer(first_lecturer, 'Python', 8)
second_student.rate_lecturer(first_lecturer, 'Вводный курс', 10)

first_reviewer = Reviewer('Best', 'Reviewer')
first_reviewer.courses_attached += ['Java']
first_reviewer.courses_attached += ['Git']
first_reviewer.rate_hw(first_student, 'Java', 8)
first_reviewer.rate_hw(first_student, 'Java', 8)
first_reviewer.rate_hw(first_student, 'Java', 8)
first_reviewer.rate_hw(first_student, 'Java', 8)
first_reviewer.rate_hw(first_student, 'Java', 8)
first_reviewer.rate_hw(second_student, 'Java', 7)  # not in courses_in_progress

first_reviewer.rate_hw(first_student, 'Git', 9)
first_reviewer.rate_hw(first_student, 'Git', 9)
first_reviewer.rate_hw(first_student, 'Git', 9)
first_reviewer.rate_hw(second_student, 'Git', 9)
first_reviewer.rate_hw(second_student, 'Git', 11)  # >10

second_reviewer = Reviewer('Good', 'Reviewer')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Вводный курс']
second_reviewer.rate_hw(first_student, 'Python', 8)
second_reviewer.rate_hw(first_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Git', 6)  # only Python and Вводный курс
second_reviewer.rate_hw(second_student, 'Вводный курс', 10)  # not in courses_in_progress

print('-------------------Студенты:')
for i in list_student:
    # print(i.grades)   # test
    print(i)

print('----Статистика по студентам:')
print(f'Сравнение студентов {first_student.name} {first_student.surname} < {second_student.name} {second_student.name} '
      f'= {first_student < second_student}')
print(
    f'Сравнение студентов {first_lecturer.name} {first_lecturer.surname} < {second_student.name} {second_student.name} '
    f'= {first_lecturer < second_student}')
print(f'Средней оценка за домашние задания по всем студентам = '
      f'{avg_course_grades(list_student):.2f}')
print(f'Средней оценка за домашние задания по всем студентам в рамках курса Вводный курс = '
      f'{avg_course_grades(list_student, "Вводный курс"):.2f}')
print(f'Средней оценка за домашние задания по всем студентам в рамках курса Python = '
      f'{avg_course_grades(list_student, "Python"):.2f}')
print(f'Средней оценка за домашние задания по всем студентам в рамках курса Git = '
      f'{avg_course_grades(list_student, "Git"):.2f}')
print(f'Средней оценка за домашние задания по всем студентам в рамках курса Java = '
      f'{avg_course_grades(list_student, "Java"):.2f}')

print('\n----------------Проверяющие:')
for i in list_reviewer:
    # print(i.grades)   # test
    print(i)

print('\n--------------------Лекторы:')
for i in list_lecturer:
    # print(i.grades)   # test
    print(i)

print('\n-----Статистика по лекторам:')
print(
    f'Сравнение лекторов {first_lecturer.name} {first_lecturer.surname} < {second_lecturer.name} {second_lecturer.name} '
    f'= {first_lecturer < second_lecturer}')
print(f'Средней оценки за лекции всех лекторов = '
      f'{avg_course_grades(list_lecturer):.2f}')
print(f'Средней оценки за лекции всех лекторов в рамках курса Вводный курс = '
      f'{avg_course_grades(list_lecturer, "Вводный курс"):.2f}')
print(f'Средней оценки за лекции всех лекторов в рамках курса Python = '
      f'{avg_course_grades(list_lecturer, "Python"):.2f}')
print(f'Средней оценки за лекции всех лекторов в рамках курса Git = '
      f'{avg_course_grades(list_lecturer, "Git"):.2f}')
print(f'Средней оценки за лекции всех лекторов в рамках курса Java = '
      f'{avg_course_grades(list_lecturer, "Java"):.2f}')

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
