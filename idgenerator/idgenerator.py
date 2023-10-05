import json
import random
import person
import sqlconnect

with open("idgenerator/fornamn.json", "r", encoding="utf-8") as f:
    names = json.loads(f.read())

with open("idgenerator/efternamn.json", "r", encoding="utf-8") as f:
    surnames = json.loads(f.read())

lst_things = ["Röd", "Blå", "Gul", "Grön", "Magenta", "Turkos",
              "Lejon", "Duv", "Gädd", "Kanin", "Struts", "Myr",
              "Kott", "Barr", "Ek", "Tall", "Asp", "Palm"
              "Sture", "Drottning", "Kungs", "Skogs"]
lst_cities = ["Stockholm", "Uppsala", "Malmö", "Göteborg", "Lund", "Kamomilla"]
lst_persons = []


def create_phone():
    phone = "073"
    for x in range(8):
        phone += str(random.randint(0, 9))
    return phone


def create_personalnum():
    num = str((random.randint(1958, 2023)))
    a = str((random.randint(101, 112)))
    num += a[1:3]
    a = str((random.randint(101, 131)))
    num += a[1:3]
    num += "-"
    a = str((random.randint(10000, 19999)))
    num += a[1:6]
    return num


def create_adress():
    adress = lst_things[random.randrange(0, len(lst_things))]
    adress += random.choice(["vägen", "gatan"])
    adress += " "
    adress += str(random.randint(1, 50))
    return adress


def create_postal():
    num = str((random.randint(100, 999)))
    num += " "
    a = str((random.randint(100, 199)))
    num += a[1:3]
    return num


def create_person():
    x = random.randint(0, len(names) - 1)
    y = random.randint(0, len(surnames) - 1)
    new_person = person.person(names[x], surnames[y], create_phone(),
                               create_personalnum(), create_adress(),
                               create_postal(), random.choice(lst_cities))

    return new_person

# for x in range(100):
    # sqlconnect.load_persons(create_person())
