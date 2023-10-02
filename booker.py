import datetime
import activity
import space
import pickle


lst_commands = ["show_actv", "show_spaces", "add_actv", "add_space",
                "clear_actv", "clear_space", "list_space", "list_name",
                "show_commands", "exit"]
lst_activities = []
with open("savedactivities.txt", "rb") as f:
    try:
        lst_activities = pickle.load(f)
    except EOFError:
        lst_activities = []

dict_spaces = {}
with open("savedspaces.txt", "rb") as f:
    try:
        dict_spaces = pickle.load(f)
    except EOFError:
        dict_spaces = {}


def checkconflict(new_activity):
    for x in lst_activities:
        if new_activity.space.name == x.space.name:
            if (new_activity.starttime < x.stoptime and
                    new_activity.stoptime > x.starttime):
                return False
    return True


def checkvalid(msg):
    print(msg)
    today = datetime.datetime.now()
    date = input("Enter date (mm/dd): ")
    time = input("Enter time (hh:mm): ")
    try:
        m = int(date[0:2])
        d = int(date[3:5])
        h = int(time[0:2])
        mi = int(time[3:5])
        returndate = datetime.datetime(today.year, m, d, h, mi)
    except ValueError:
        returndate = checkvalid("Invalid input, please try again")
    if returndate.date() < today.date():
        returndate = checkvalid("Date has already passed, please try again")

    return returndate


def checkspaces():
    while True:
        indata = input("Enter name of space: ")
        if indata in dict_spaces:
            return indata


def newbooking():
    while True:
        name = input("Enter name: ")
        space = checkspaces()
        starttime = checkvalid("Enter starttime: ")
        stoptime = checkvalid("Enter stoptime: ")
        if starttime > stoptime:
            print("Invalid stoptime, please try again")
            continue
        new_activity = activity.activity(name, dict_spaces[space],
                                         starttime, stoptime)
        if checkconflict(new_activity):
            lst_activities.append(new_activity)
        else:
            print("Schedule error")
            continue
        new_activity.set_people()
        break
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


def show_activities():
    print("-" * 30)
    for x in lst_activities:
        print(x)
        print("-" * 30)


def show_spaces():
    for y in dict_spaces:
        print(y)


def show_commands():
    for x in lst_commands:
        print(x)


while True:
    indata = input("> ")
    if indata == lst_commands[0]:
        show_activities()
    elif indata == lst_commands[1]:
        show_spaces()
    elif indata == lst_commands[2]:
        newbooking()
    elif indata == lst_commands[3]:
        newspace()
    elif indata == lst_commands[4]:
        lst_activities.clear()
    elif indata == lst_commands[5]:
        dict_spaces.clear()
    elif indata == lst_commands[6]:
        listspace()
    elif indata == lst_commands[7]:
        listnames()
    elif indata == lst_commands[8]:
        show_commands()
    elif indata == lst_commands[9]:
        break

with open("savedactivities.txt", "wb") as f:
    pickle.dump(lst_activities, f)

with open("savedspaces.txt", "wb") as f:
    pickle.dump(dict_spaces, f)
