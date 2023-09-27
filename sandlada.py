import pickle


class test:
    def __init__(self, name):
        self.name = name


testobj = test("testbojekthej")
with open("savedactivities.py", "wb") as f:
    pickle.dump(testobj, f)
