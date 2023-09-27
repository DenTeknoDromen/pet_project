import datetime
import activity
import space
import pickle

lst_activities = []
with open("savedactivities.txt", "rb") as f:
    lst_activities = pickle.load(f)

dict_spaces = {}
with open("savedspaces.txt", "rb") as f:
    dict_spaces = pickle.load(f)


def checkconflict(lst_activities, new_activity):
    for x in lst_activities:
        if new_activity.space.name == x.space.name:
            if (new_activity.starttime < x.stoptime and
                    new_activity.stoptime > x.starttime):
                return False
    return True


def newbooking():
    name = input("Enter name: ")
    space = input("Enter room: ")
    starttime = input("Enter starttime (xx:xx): ")
    stoptime = input("Enter stoptime (xx:xx): ")
    start = datetime.time(int(starttime[0:2]), int(starttime[3:5]))
    stop = datetime.time(int(stoptime[0:2]), int(stoptime[3:5]))

    new_activity = activity.activity(name, dict_spaces[space], start, stop)
    if checkconflict(lst_activities, new_activity):
        lst_activities.append(new_activity)
    else:
        print("Schedule error")
    print("-" * 30)


def newspace():
    name = input("Enter name: ")
    spc_newspace = space.space(name)
    dict_spaces[name] = spc_newspace


def listspace():
    indata = input("Enter name of space: ").casefold()
    print("-" * 30)
    for x in lst_activities:
        if (x.space.name.casefold() in indata or
                indata in x.space.name.casefold()):
            print(x)
            print("-" * 30)


def listnames():
    indata = input("Enter name: ").casefold()
    print("-" * 30)
    for x in lst_activities:
        if indata in x.name.casefold() or x.name.casefold() in indata:
            print(x)
            print("-" * 30)


while True:
    indata = input("> ")
    if indata == "show":
        print("-" * 30)
        for x in lst_activities:
            print(x)
            print("-" * 30)
    elif indata == "showspaces":
        for y in dict_spaces:
            print(y)
    elif indata == ("add"):
        newbooking()
    elif indata == "addspace":
        newspace()
    elif indata == ("clear"):
        lst_activities.clear()
    elif indata == "clearspace":
        dict_spaces.clear()
    elif indata == "listspace":
        listspace()
    elif indata == "listname":
        listnames()
    elif indata == "exit":
        break

with open("savedactivities.txt", "wb") as f:
    pickle.dump(lst_activities, f)

with open("savedspaces.txt", "wb") as f:
    pickle.dump(dict_spaces, f)
