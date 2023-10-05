import datetime
import json


class activity:
    def __init__(self, name, space, starttime, until):
        self.name = name
        self.space = space
        self.date = starttime.date()
        self.time = starttime.time()
        self.until = until
        self.people = {}

    def __str__(self):
        self_str = (f"{self.name} i {self.space}\n"
                    f"{self.date.strftime('%b %e %Y')}\n"
                    f"kl {self.time.strftime('%H:%M')} - "
                    f"{self.until.strftime('%H:%M')}\n")
        if len(self.people) > 0:
            for keys in self.people:
                self_str += f"{keys}(s): \n"
                for values in self.people[keys]:
                    self_str += f"\t{values}\n"
        return self_str

    def get_jsonmembers(self):
        return json.dumps(self.people)

    def add_role(self):
        while True:
            indata = input("Enter name of new role: ")
            if indata not in self.people:
                return indata
            else:
                print("Role already exists, enter new role: ")

    def add_member(self, key):
        while True:
            indata = input(f"Enter name of new {key.casefold()}(s): ")
            return indata

    def set_people(self):
        if len(self.people) == 0:
            self.people[self.add_role()] = []

        for keys in self.people.keys():
            print(keys)

        indatakey = input("Choose role to add people to: ")
        self.people[indatakey].append(self.add_member(indatakey))
