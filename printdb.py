from persistence import *
from persistence import _Employees


def printdata():
    print('Activities')
    act=repo.Activities.find_all()
    for x in act:
        s="(%d, %d, %d, %d)"%(x.product_id,x.quantity,x.activator_id,x.date)
        print(s)
    print('Coffee_stands')
    act = repo.Coffee_stands.find_all()
    for x in act:
        s = "(%d, '%s', %d)" % (x.id, x.location, x.number_of_employees)
        print(s)
    print('Employees')
    act = repo.Employees.find_all()
    for x in act:
        s = "(%d, %s, %g, %g)" % (x.id, x.name, x.salary, x.coffee_stand)
        print(s)
    print('Products')
    act = repo.Products.find_all()
    for x in act:
        s = "(%d, %s, %g, %d)" % (x.id,x.description,x.price,x.quantity)
        print(s)
    print('Suppliers')
    act = repo.Suppliers.find_all()
    for x in act:
        s = "(%d, %s, %s)" % (x.id, x.name, x.contact_information)
        print(s)
    print('Employees report')
    print(repo.Employees.__str__())

