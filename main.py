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

# s1 = Student("Иван", "Воробьев", 17, 5.5)
# s1.surname = "Васильев"
# print(s1)
#
# s2 = Student("Алексей", "Курков", 18, 3.2)
# print(s2)
#
# if s1 > s2:
#     print(f"Средний балл первого студента {s1.average_point} больше среднего балла второго студента {s2.average_point}")
#
# elif s1 < s2:
#     print(f"Средний балл первого студента {s1.average_point} меньше среднего балла второго студента {s2.average_point}")
#
# elif s1 == s2:
#     print(f"Средний балл первого студента {s1.average_point} равен среднему баллу второго студента {s2.average_point}")


# Задача №2.
# В данной задаче вам предстоит изучить и применить концепции объектно-ориентированного программирования (ООП)
# на практике. Вы будете моделировать часть предметной области — библиотеку, используя язык UML 2.0
# для построения диаграммы классов.
# Ваша цель — понять и реализовать отношения между классами, такие как зависимость, агрегирование и композиция.
# В качестве примера предметной области выбрана библиотека, где вам предстоит создать классы для моделирования
# библиотеки, книг, сотрудников, жанров и контактной информации. После того как вы построите диаграмму
# классов, вам нужно будет написать на языке Python реализацию строго по диаграмме.

class Library:

    __library_name: str
    __address: str
    __list_books: list[Book]
    __list_employees: list["Employee"]

    def __init__(self, library_name: str, address: str):

        if not isinstance(library_name, str):
            raise ValueError("__library_name должно быть строкой")

        if not isinstance(address, str):
            raise ValueError("__address должно быть строкой")

        self.__library_name = library_name
        self.__address = address
        self.__list_books = []
        self.__list_employees = []

    def __str__(self):
        return (f"Библиотека: {self.__library_name}, находящаяся по адресу: {self.__address}.\n"
                f"Список книг: {self.__list_books}.\n"
                f"Сотрудники: {self.__list_employees}")

    def _get_library_name(self):
        return self.__library_name

    def _get_address(self):
        return self.__address

    def _get_list_books(self):
        return self.__list_books

    def _get_list_employees(self):
        return self.__list_employees

    def _set_address(self, new_address):
        self.__address = new_address

    def _set_library_name(self, new_libray_name):
        self.__library_name = new_libray_name

    def add_book(self, book: "Book"):

        if isinstance(book, Book):

            if book not in self.__list_books:
                self.__list_books.append(book)

        else: raise ValueError()

    def remove_book(self, book: Book):

        if book in self.__list_books:
            self.__list_books.remove(book)

    def add_employee(self, employee: "Employee"):

        if isinstance(employee, Employee):

            if employee not in self.__list_employees:
                self.__list_employees.append(employee)

        else: raise ValueError()

    def remove_employee(self, employee: "Employee"):

         if employee in self.__list_employees:
             self.__list_employees.remove(employee)


    library_name = property(_get_library_name, _set_library_name)
    address = property(_get_address, _set_address)


class Book:

    ID_counter = 1

    __title: str
    __autor: str
    __year_publication: int
    __id: int
    __list_genre: list[Genre]
    def __init__(self, title: str, autor:str, year_publication: int):

        if not isinstance(title, str): raise ValueError("title должна быть строкой")
        if not isinstance(autor, str): raise ValueError("autor должна быть строкой")
        if not isinstance(year_publication, int): raise ValueError("year_publication должна быть числом int")

        self.__title = title
        self.__autor = autor
        self.__year_publication = year_publication
        self.__id = Book.ID_counter
        Book.ID_counter += 1
        self.__list_genre = []

    def __str__(self):
        return (f"Название книги: {self.__title}\n"
                f"Автор: {self.__autor}\n"
                f"Год издания: {self.__year_publication} г.\n"
                f"Жанр: {self.__list_genre}; ID книги: {self.__id}")

    def __repr__(self):
        return f"'{self.__title}' ({self.__autor})"

    def get_title(self):
        return self.__title

    def get_autor(self):
        return self.__autor

    def get_year(self):
        return self.__year_publication

    def get_id(self):
        return self.__id

    def get_list_genres(self):
        return self.__list_genre

    def set_year(self, new_year):

        if new_year != self.__year_publication:
            self.__year_publication = new_year

    def add_genre(self, genre: Genre):

        if isinstance(genre, Genre):

            if genre not in self.__list_genre:
                self.__list_genre.append(genre)

        else: raise ValueError()

    def remove_genre(self, genre: Genre):

        if genre in self.__list_genre:
            self.__list_genre.remove(genre)


class Genre:

    __genre_book: str
    __genre_description: str
    def __init__(self, genre_book: str, genre_description: str):

        self.__genre_book = genre_book
        self.__genre_description = genre_description

    def __str__(self):
        return f"Жанр книги: {self.__genre_book}; Описание жанра {self.__genre_description}"

    def __repr__(self):
        return f"{self.__genre_book}"

    def get_name_genre(self):
        return self.__genre_book

    def get_genre_description(self):
        return self.__genre_description

    def set_name_genre(self, genre):

        if genre not in self.__genre_book:
            self.__genre_book = genre


class ContactInfo:

    __type_address: str
    __value_address: str
    __type_telephone_number: str
    __value_telephone_number: int
    __type_email: str
    __value_email: str

    def __init__(self, type_address: str, value_address: str, type_telephone_number: str, value_telephone_number: str, type_email: str, value_email: str):

        if not isinstance(value_telephone_number, str): raise ValueError("value_telephone_number -должна быть строкой")

        self.__type_address = type_address
        self.__value_address = value_address
        self.__type_telephone_number = type_telephone_number
        self.__value_telephone_number = value_telephone_number
        self.__type_email = type_email
        self.__value_email = value_email

    def __str__(self):
        return (f"{self.__type_address}: {self.__value_address}\n"
                f"{self.__type_telephone_number}: {self.__value_telephone_number}\n"
                f"{self.__type_email}: {self.__value_email}")

    def __repr__(self):
        return f"Contact({self.__value_email})"

    def get_value_address(self):
        return self.__value_address

    def get_value_telephone_number(self):
        return self.__value_telephone_number

    def get_value_email(self):
        return self.__value_email

    def set_value_telephone_number(self, number):
        if number not in self.__value_telephone_number:
            self.__value_telephone_number = number

    def set_value_address(self, address):
        if not address in self.__value_address:
            self.__value_address = address

    def set_value_email(self, email):
        if email not in self.__value_email:
            self.__value_email = email

class Employee:

    ID_employee = 1
    __name: str
    __post: str
    __id_employee: int
    __contactinfo: ContactInfo

    def __init__(self, name: str, post: str):

        self.__name = name
        self.__post = post
        self.__id_employee = Employee.ID_employee
        Employee.ID_employee += 1
        self.__contactinfo = None

    def __str__(self):
        return (f"Сотрудник имя: {self.__name}\n"
                f"Должность: {self.__post}; ID сотрудника: {self.__id_employee}\n"
                f"Контактная информация: {self.__contactinfo}")

    def __repr__(self):
        return f"{self.__name} ({self.__post})"

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__post

    def get_id(self):
        return self.__id_employee

    def get_contact_info(self):
        return self.__contactinfo

    def set_position(self, position):
        self.__post = position

    def add_contact_info(self, contact: "ContactInfo"):

        if isinstance(contact, ContactInfo):

            self.__contactinfo = contact

        else: raise ValueError()

    def remove_contact_info(self):

        self.__contactinfo = None


# Задача №3.
# Вы хотите создать систему для управления автосалоном. В этом автосалоне продается множество различных автомобилей
# разных брендов, моделей и годов выпуска. Также у вас есть продавцы, которые работают в салоне, и клиенты, которые
# приходят покупать или заказывать автомобили.
# Ваша задача сформировать диаграмму классов, разработать эти классы и написать сценарии использования объектов этих
# классов. Например, вы можете создать несколько автомобилей, продавцов и клиентов, зарегистрировать их в автосалоне,
# продать автомобиль клиенту через продавца, изменить цену автомобиля и т.д.

class Car:

    CONST_SOLD = 0  # Продана
    CONST_EXPECTED = 1  # Ожидается
    CONST_IS_STOCK = 2  # В наличии

    __brand: str
    __model: str
    __year_manufacture: int
    __price: float
    __status: int

    def __init__(self, brand: str, model: str, year_manufacture: int, price: float, status: int = CONST_IS_STOCK):

        if not isinstance(status, int) or not 0 <= status <= 2: raise ValueError("Статус должен быть натуральное числом в диапазоне от 0 до 2")

        self.__brand = brand
        self.__model = model
        self.__year_manufacture = year_manufacture
        self.__price = price
        self.__status = status

    def __str__(self):

        status_info = ""
        if self.__status == self.CONST_SOLD: status_info = "Нет в наличии. Продано"
        elif self.__status == self.CONST_EXPECTED: status_info = "Ожидается"
        elif self.__status == self.CONST_IS_STOCK: status_info = "В наличии"

        return (f"Автомобиль марка/модель: {self.__brand} {self.__model}\n"
                f"Год выпуска: {self.__year_manufacture} г.\n"
                f"Стоимость: {self.__price} руб.\n"
                f"Статус: {status_info}")

    def __repr__(self):
        return f"Автомобиль: {self.__brand} {self.__model}, {self.__year_manufacture} г.в.; "

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year_manufacture

    def get_price(self):
        return self.__price

    def get_status(self):
        return self.__status

    def set_brand(self, new_brand):

        if not isinstance(new_brand, str): raise ValueError("Бренд должен быть строкой")
        self.__brand = new_brand

    def set_model(self, new_model):

        if not isinstance(new_model, str): raise ValueError("Модель должна быть строкой")
        self.__model = new_model

    def set_year(self, new_year):

        if not isinstance(new_year, int) and not (1900 < new_year): raise ValueError("Год должен быть натуральным числом от 1900 года и выше")
        self.__year_manufacture = new_year

    def set_price(self, new_price):

        if not isinstance(new_price, float) and not (0 < new_price): raise ValueError("Цена должна быть натуральным числом больше нуля")
        self.__price = new_price


class Salesperson:

    __name: str
    __work_experience: float
    __list_car: list[Car]
    def __init__(self, name: str, work_experience: float):

        self.__name = name
        self.__work_experience = work_experience
        self.__list_car: list [Car] = []

    def __str__(self):
        return f"Сотрудник: {self.__name}; Опыт работы: {self.__work_experience} г; Список проданных авто: {self.__list_car}"

    def get_name(self):
        return self.__name

    def get_work_experience(self):
        return self.__work_experience

    def get_car(self):
        return self.__list_car

    def set_name(self, new_name):

        if not isinstance(new_name, str): raise ValueError("Имя должно быть строкой")
        self.__name = new_name

    def set_work_experience(self, new_experience):

        if not isinstance(new_experience, int | float): raise ValueError("Опыт должен быть float")
        self.__work_experience = float(new_experience)

    def add_car(self, new_car):

       if not isinstance(new_car, Car): raise ValueError("Объект должен быть Car")
       self.__list_car.append(new_car)

    def remove_car(self, car):

        self.__list_car.remove(car)


car1 = Car("Toyota", "Crown", 2026, 7000000, 2)
print(car1)
print("-" * 10)
car2 = Car("BMW", "X8", 2024, 5500000.20, 0)
print(car2)
sal = Salesperson("Витя", 2.5)
sal.add_car(car1)
sal.add_car(car2)
print(sal)
print(sal.get_car())
price = car1.get_price() + car2.get_price()
print(Car.get_price(car1))
print(Car.get_price(car2))
print(price)
