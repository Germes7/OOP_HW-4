from __future__ import annotations


# Модуль 3. Задание 4

# Задача №1
# Сформируйте класс Student, для работы с сущностью «Студент». Класс состоит из следующих полей:
# имя, фамилию, возраст и средний балл студента.
# Реализуйте методы get и set для каждого поля, а также метод str, который будет возвращать строковое
# представление объекта класса "Студент".
# Переопределите операторы сравнения (==, !=, <, >, <=, >=) для сравнения студентов по их среднему баллу.

class Student:

    __name: str
    __surname: str
    __age: int
    average_point: float

    def __init__(self, name: str, surname: str, age: int, average_point: float):

        if not isinstance(age, int):
            raise ValueError("Введите число")

        self.__name = name
        self.__surname = surname
        self.__age = age
        self.average_point = average_point

    def __str__(self):

        return f"Студент: {self.__name} {self.__surname}. Возраст {self.__age} лет. Средний балл: {self.average_point} баллов"

    def _get_name(self):
        return self.__name

    def _get_surname(self):
        return self.__surname

    def _get_age(self):
        return self.__age

    def _get_average_point(self):
        return self.average_point

    def _set_name(self, name):
        self.__name = name

    def _set_surname(self, surname):
        self.__surname = surname

    def _set_age(self, age):
        if not isinstance(age, int):
            raise ValueError("Введите число")

        self.__age = age

    def __eq__(self, other):
        return self.average_point == other.average_point

    def __ne__(self, other):
        return self.average_point != other.average_point

    def __lt__(self, other):
        return self.average_point < other.average_point

    def __gt__(self, other):
        return self.average_point > other.average_point

    def __le__(self, other):
        return self.average_point <= other.average_point

    def __ge__(self, other):
        return self.average_point >= other.average_point

    name = property(_get_name, _set_name)
    surname = property(_get_surname, _set_surname)
    age = property(_get_age, _set_age)

s1 = Student("Иван", "Воробьев", 17, 5.5)
s1.surname = "Васильев"
print(s1)

s2 = Student("Алексей", "Курков", 18, 3.2)
print(s2)

if s1 > s2:
    print(f"Средний балл первого студента {s1.average_point} больше среднего балла второго студента {s2.average_point}")

elif s1 < s2:
    print(f"Средний балл первого студента {s1.average_point} меньше среднего балла второго студента {s2.average_point}")

elif s1 == s2:
    print(f"Средний балл первого студента {s1.average_point} равен среднему баллу второго студента {s2.average_point}")
