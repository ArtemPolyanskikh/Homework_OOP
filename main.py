from functools import total_ordering


@total_ordering
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_st(self, lectur, corses, grades):
        if isinstance(lectur, Lecturer) and corses in lectur.courses_attached:
            if corses in lectur.grades:
                lectur.grades[corses] += [grades]
            else:
                lectur.grades[corses] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашнее задание: {self.av_rat_st}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}  
Завершенные курсы: {', '.join(self.finished_courses)} """

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.av_rat_st == other.av_rat_st

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.av_rat_st < other.av_rat_st

    @property
    def av_rat_st(self):
        rat_list = []
        for val in self.grades.values():
            for i in val:
                rat_list.append(i)
        if not rat_list:
            return 'Оценочный лист пуст'
        else:
            return sum(rat_list) / len(rat_list)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


@total_ordering
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    @property
    def av_rat(self):
        rat_list = []
        for val in self.grades.values():
            for i in val:
                rat_list.append(i)
        if not rat_list:
            return 'Оценочный лист пуст'
        else:
            return sum(rat_list) / len(rat_list)

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка: {self.av_rat}"""

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.av_rat == other.av_rat

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.av_rat < other.av_rat


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}"""



def average_gr_st(stud, corses):
    res = []
    for st in stud:
        if isinstance(st, Student) and corses in st.grades:
            mid_res = [x for x in st.grades[corses]]
            res.append(sum(mid_res) / len(mid_res))
        else:
            return 'Ошибка'
    return sum(res) / len(res)


def average_gr_lect(lector, corses):
    res = []
    for lc in lector:
        if isinstance(lc, Lecturer) and corses in lc.grades:
            mid_res = [x for x in lc.grades[corses]]
            res.append(sum(mid_res) / len(mid_res))
        else:
            return 'Ошибка'
    return sum(res) / len(res)


a = Student('bob', 'smit', 'men')
a2 = Student('Bill', 'Murrey', 'men')
a.add_courses('1C')
a2.add_courses('C#')
a.add_courses('Basik')
a2.add_courses('Paskal')
a.courses_in_progress += ['Python']
a2.courses_in_progress += ['Python']


r = Reviewer('Vit', 'Pupkin')
r2 = Reviewer('Nadejda', 'Konstantinovna')

r.courses_attached += ['Python']
r2.courses_attached += ['Python']

r.rate_hw(a, 'Python', 7)
r.rate_hw(a, 'Python', 8)
r.rate_hw(a, 'Python', 9)
r2.rate_hw(a2, 'Python', 2)
r2.rate_hw(a2, 'Python', 6)
r2.rate_hw(a2, 'Python', 10)
# print(r)
# print(r2)



l = Lecturer('Gedeon', 'Vasilich')
l2 = Lecturer('Evanessa', 'Rudolfovna')
l.courses_attached += ['Python']
l2.courses_attached += ['Python']
a.rate_st(l, 'Python', 10)
a.rate_st(l, 'Python', 6)
a2.rate_st(l2, 'Python', 7)
a2.rate_st(l2, 'Python', 6)


print(l)
print(l2)


print(average_gr_st([a, a2], 'Python'))
print(average_gr_lect([l, l2], 'Python'))
