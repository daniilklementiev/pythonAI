'''
1. Разработать класс. который будет представлять собой описание студента.
Конструктор должен притнимать имя и фамилию студента, а также одну из 3 
специальностей: программирование, администрирование или дизайн. Если специальность
не задана, то полю присвается значение по умолчанию "базовый".
Одним из полей класса является контейнер, который может хранить предметы и экзаменационную 
оценку по нему.
Реализовать в классе методы добавления предмета и оценки, а также метода gpa(), который
будет возвращать средний бал студента или 0, если в контейнере нет информации об экзаменах.


2. Из курсе алгебры повторить следующие темы: уравнение прямой, коэффициент наклона, 
производная функции, минимальное и максимальное значение функции. Быть готовым к тесту,
на котором будет предложено решить несколько простых задач на эти темы.
'''

class Student:
    def __init__(self, name, surname, speciality="basic"):
        self.name = name
        self.surname = surname
        self.speciality = speciality
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def gpa(self):
        if self.marks:
            return sum(self.marks.values())/len(self.marks)
        else:
            return 0

def printer(*numbers):
    for a in numbers:
        print(a)

def printer2(**kwargs):  # keyword arguments
    for var, value in kwargs.items():
        print(f"{var} = {value}")


def sample(a, b, *args, t=1, **kwargs):
    pass

def summa(a, b):
    return a+b
        
printer2(n1 = 5, n2 = 10)

#r = summa(a=3, b=4)
#print(r)

class Person: 
    def __init__(self, name = 'James Bond', age = 35, location = 'London'):     # Constructor
        self.name = name
        self.age = age
        self.location = location

    def print(self):
        print(f"My name is {self.name}")
    
spy = Person('James Bond')

spy.print()