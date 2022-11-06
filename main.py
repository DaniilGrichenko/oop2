#1 Make the class with composition.
class Laptop:
    def __init__(self):
        battery_1 = Battery('This is battery 1 (4000)')
        battery_2 = Battery('This is battery 2 (4600)')
        battery_3 = Battery('This is battery 3 (3700)')
        self.laptop = [battery_1.charger, battery_2.charger, battery_3.charger]


class Battery:
    def __init__(self, charger):
        self.charger = charger


laptop = Laptop()
print(laptop.laptop)


#2 Make the class with aggregation


class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self, strength):
        self.strength = strength


Guitar_string = GuitarString(f" strength {85}%")
First_Guitar = Guitar(Guitar_string.strength)
print(First_Guitar.guitar_string)


# 3 Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.


class Calc:
    def __init__(self, first: int, second: int, third: int):
        self.first = first
        self.second = second
        self.third = third

    def add_nums(self):
        return self.first + self.second + self.third

# Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
#     Він повинен мати 2 методи:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#
# 4 Task


class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.ingredients)
pasta_2 = Pasta.bolognaise()
print(pasta_2.ingredients)

# 5
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """
# 5


class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value > Concert.max_visitors_num:
            self._visitors_count = Concert.max_visitors_num
        else:
            self._visitors_count = value


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)


# 6.
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
#     """


import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


# 7. Create the same class (6) but using NamedTuple
from collections import namedtuple
AddressBook = namedtuple('AddressBook', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])


# 8.
# class AddressBook:
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
# 8.

class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age


    def __repr__(self):
        return f'address_book(key= {self.key}, name= {self.name}, phone_number= {self.phone_number},' \
               f'address= {self.address}, email= {self.email}, birthday= {self.birthday}, age= {self.age})'


contact = AddressBook(1234, 'Daniil', '096232****', 'UA', 'test-test@ukr.net', '02.02.2004', 18)
print(contact)


# 9.
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"
# 9.

class Person:
    name = "John"
    age = 36
    country = "USA"


Person.age = 63
print(Person.age)

# 10.
# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
# 10.


class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(7, 'Egor')
setattr(student, 'email', 'egor@ukr.net')
student_email = getattr(student, 'email')
print(student_email)