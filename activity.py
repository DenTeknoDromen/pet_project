class activity:
    def __init__(self, name, space, starttime, stoptime):
        self.name = name
        self.space = space
        self.starttime = starttime
        self.stoptime = stoptime

    def __str__(self):
        return (f"{self.name} i {self.space}\n"
                f"klockan {self.starttime} - {self.stoptime}")
