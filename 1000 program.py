# Calculator Program

def add_num(a, b):
    sum=a+b
    print("The sum of" ,a, "and" ,b, "is :",sum)
def sub_num(a, b):
    sub=a-b
    print("The subtraction of" ,a, "and" ,b, "is :",sub)
def mul_num(a, b):
    mul=a*b
    print("The multiplication of" ,a, "and" ,b, "is :",mul)
def div_num(a, b):
    div=a/b
    if div==0:
        print("The divide of" ,a, "and" ,b, "is : 0")
    else:
        print("The divide of" ,a, "and" ,b, "is :",div)
     
choice = input("Enter Choice (+, -, *, /): ")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
if choice == "+":
    add_num(a, b)
elif choice == "-":
    sub_num(a, b)
elif choice == "*":
    mul_num(a, b)
elif choice == "/":
    div_num(a, b)
else:
    print("Invalid Choice! Please enter +, -, *, or /.")

# Program of Class
class student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def show (self):
        print("ID",self.id)
        print("Name",self.name)
student1= student(858157,"Mahin")
student2= student(858156,"Shad")
student1.show()
student2.show()

# Largest number in class
class LargestNumber:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def find_largest(self):
        if self.a > self.b and self.a > self.c:
            print("A is the largest number")
        elif self.b > self.a and self.b > self.c:
            print("B is the largest number")
        else:
            print("C is the largest number")
a = int(input("Enter a value of a: "))
b = int(input("Enter a value of b: "))
c = int(input("Enter a value of c: "))
largest_number = LargestNumber(a, b, c)
largest_number.find_largest()

# roots program in class
import math
class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def roots(self):
        d = self.b ** 2 - 4 * self.a * self.c
        if d == 0:
            x1 = -self.b / (2 * self.a)
            x2 = x1
            print("Roots are real and the values are :")
            print("x1 =", x1)
            print("x2 =", x2)
        elif d > 0:
            x1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(d)) / (2 * self.a)
            print("Roots are real and the values are :")
            print("x1 =", x1)
            print("x2 =", x2)
        else:
            print("Roots are imaginary!")
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))
equation = Equation(a, b, c)
equation.roots() 

#triangle in class
import math
class TriangleArea:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calculate_area(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b):
            s = (self.a + self.b + self.c) / 2
            area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
            return area
        else:
            return None
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
triangle = TriangleArea(a, b, c)
area = triangle.calculate_area()
if area is not None:
    print("Triangle Area =", area)
else:
    print("Triangle is not possible")

#Ciclearea program
import math
class Circle:
    def __init__(self, r):
        self.r = r
    def calculate_area(self):
        return math.pi * self.r * self.r
r = float(input("Enter the value of r: "))
circle = Circle(r)
area = circle.calculate_area()
print("The area of the circle is:", area)

# Save data in file
mahin= "data.txt"
file = open(mahin, "w")
file.write("Hello world!\n")
file.write("Py are great not python")
file.close()
print("iam done")
file = open(mahin, "r")
okay= file.read()
file.close()
print("\n is it right program")
print(okay) 