import sqlite3
import atexit
from dbtools import Dao

# Data Transfer Objects:
class _Employees(object):
    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand

class _Suppliers(object):
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information

class _Products(object):
    def __init__(self, id, description, price , quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity

class _Coffee_stands(object):
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees

class _Activities(object):
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date

# # Data Access Objects:
# # All of these are meant to be singletons
# class _Students:
#     def __init__(self, conn):
#         self._conn = conn
#
#     def insert(self, student):
#         self._conn.execute("""
#                INSERT INTO students (id, name) VALUES (?, ?)
#            """, [student.id, student.name])
#
#     def find(self, student_id):
#         c = self._conn.cursor()
#         c.execute("""
#             SELECT id, name FROM students WHERE id = ?
#         """, [student_id])
#
#         return Student(*c.fetchone())
#
#
# class _Assignments:
#     def __init__(self, conn):
#         self._conn = conn
#
#     def insert(self, assignment):
#         self._conn.execute("""
#                 INSERT INTO assignments (num, expected_output) VALUES (?, ?)
#         """, [assignment.num, assignment.expected_output])
#
#     def find(self, num):
#         c = self._conn.cursor()
#         c.execute("""
#                 SELECT num,expected_output FROM assignments WHERE num = ?
#             """, [num])
#
#         return Assignment(*c.fetchone())
#
#
# class _Grades:
#     def __init__(self, conn):
#         self._conn = conn
#
#     def insert(self, grade):
#         self._conn.execute("""
#             INSERT INTO grades (student_id, assignment_num, grade) VALUES (?, ?, ?)
#         """, [grade.student_id, grade.assignment_num, grade.grade])
#
#     def find_all(self):
#         c = self._conn.cursor()
#         all = c.execute("""
#             SELECT student_id, assignment_num, grade FROM grades
#         """).fetchall()
#
#         return [Grade(*row) for row in all]


# The Repository
class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.employees = Dao(_Employees, self._conn)
        self.suppliers = Dao(_Suppliers, self._conn)
        self.products = Dao(_Products, self._conn)
        self.coffee_stands = Dao(_Coffee_stands, self._conn)
        self.activities = Dao(_Activities, self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
            _conn.executescript("""
            CREATE TABLE employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                salary REAL NOT NULL,
                coffee_stand INTEGER REFERENCES Coffee_stands(id)
            );

            CREATE TABLE suppliers (
                id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL,
                contact_information TEXT
            );

            CREATE TABLE products (
                id INTEGER PRIMARY KEY,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            );

            CREATE TABLE coffee_stands (
                id INTEGER PRIMARY KEY,
                location TEXT NOT NULL,
                number_of_employees INTEGER
            );

            CREATE TABLE activities (
                product_id INTEGER INTEGER REFERENCES Products(id),
                quantity INTEGER NOT NULL,
                date DATE NOT NULL,
                activator_id INTEGER NOT NULL
            );
        """)


# see code in previous version...

# the repository singleton
repo = _Repository()
atexit.register(repo._close)