# OOP of four piller program.
class Animal:
    def __init__(self,name):
        self.name=name
        print(self.name+" was adopted.")
    def run(self):
        print("running")
class Turtle(Animal):
    def run(self):
        print("because her parents are gone in river.")
tur=Turtle("tur")
tur.run()