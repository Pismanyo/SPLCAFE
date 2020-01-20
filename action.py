from persistence import *
def action(file):
    configfile = open("action.txt", "r")
    for x in configfile:
        line = x.split(", ")
        firstLetter = x.split(", ")[0]
        run=Activitie(line[0], line[1], line[2],line[3])
        repo.Activities.insert(run)
        a=repo.Products.find(line[0])
        if a.quantity+line[1]>=0:
            a.quantity=a.quantity+line[1]






    run=repo.Activities.find_all(line[0])



