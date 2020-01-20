import sqlite3
import os
import dbtools
from persistence import *
import printdb
def main():
   r = repo.create_tables()
   configfile = open("config.txt", "r")
   for x in configfile:
       line = x.split(", ")
       firstLetter = x.split(", ")[0]
       if firstLetter == 'P':
           repo.Products.insert(Product(line[1],line[2],line[3], 0))
       elif firstLetter == 'S':
           repo.Suppliers.insert(Supplier(line[1],line[2],line[3].strip()))
       elif firstLetter == 'E':
           repo.Employees.insert(Employee(line[1],line[2],line[3],line[4]))
       elif firstLetter == 'C':
           repo.Coffee_stands.insert(Coffee_stand(line[1],line[2],line[3]))

if __name__ == "__main__":
    main()
    printdb.printdata()

