import sqlite3
import atexit
from dbtools import Dao

# Data Transfer Objects:
class Employee(object):
    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand

class Supplier(object):
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information

class Product(object):
    def __init__(self, id, description, price , quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity

class Coffee_stand(object):
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees

class Activity(object):
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date

# Data Access Objects:
# All of these are meant to be singletons
class _Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
               INSERT INTO Employees (id, name, salary, coffee_stand) VALUES (?, ?, ?, ?)
           """, [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, employee_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id , name, salary, coffee_stand FROM Employees WHERE id = ?
        """, [employee_id])

        return Employee(*c.fetchone())


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO Suppliers (id, name, contact_information) VALUES (?, ?, ?)
        """, [supplier.id, supplier.name, supplier.contact_information])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id, name, contact_information FROM Suppliers WHERE id = ?
            """, [supplier_id])

        return Supplier(*c.fetchone())


class _Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
            INSERT INTO Products (id, description, price, quantity) VALUES (?, ?, ?, ?)
        """, [product.id, product.description, product.price, product.quantity])

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, description, price, quantity FROM Products
        """).fetchall()

        return [Product(*row) for row in all]

class _Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    # def insert(self, coffee_stand):
    #     self._conn.execute("""
    #            INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)
    #        """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    def find(self, coffee_stand_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id , location, number_of_employees FROM Coffee_stands WHERE id = ?
        """, [coffee_stand_id])

        return Coffee_stand(*c.fetchone())

class _Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activity):
        self._conn.execute("""
               INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
           """, [activity.product_id, activity.quantity, activity.activator_id, activity.date])

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT product_id, quantity, activator_id, date FROM Activities
        """).fetchall()

        return [Activity(*row) for row in all]
# The Repository
class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.Employees = Dao(Employee, self._conn)
        self.Suppliers = Dao(Supplier, self._conn)
        self.Products = Dao(Product, self._conn)
        self.Coffee_stands = Dao(Coffee_stand, self._conn)
        self.Activities = Dao(Activity, self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
            self._conn.executescript("""
            DROP TABLE IF EXISTS Employees;
            CREATE TABLE Employees (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                salary REAL NOT NULL,
                coffee_stand INTEGER REFERENCES Coffee_stands(id)
            );

            DROP TABLE IF EXISTS Suppliers;
            CREATE TABLE Suppliers (
                id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL,
                contact_information TEXT
            );

            DROP TABLE IF EXISTS Products;
            CREATE TABLE Products (
                id INTEGER PRIMARY KEY,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            );

            DROP TABLE IF EXISTS Coffee_stands;
            CREATE TABLE Coffee_stands (
                id INTEGER PRIMARY KEY,
                location TEXT NOT NULL,
                number_of_employees INTEGER
            );

            DROP TABLE IF EXISTS Activities;
            CREATE TABLE Activities (
                product_id INTEGER INTEGER REFERENCES Products(id),
                quantity INTEGER NOT NULL,
                date DATE NOT NULL,
                activator_id INTEGER NOT NULL
            );
        """)

repo = _Repository()
atexit.register(repo._close)