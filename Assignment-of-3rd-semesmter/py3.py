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

# iterator program.
iter_list=iter(["Computer","Science","And","Technology"])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))

# working procedure of itarator>>>
a =[0,5,10,14,20]
for i in  a:
    if i%2==0:
        print(str(i) + " is even number")
    else:
        print(str(i) + " is odd number")