
print("Hello World!")

print ("double quotation")
print ('here is the single')
print ("single quote - ' in a double quoted string")
print ('double quotes - " in a single quoted string')
print ("here comes the escaped quotes - \"")
print ('here is the single one - \'')
print (""" This is a paragraph. This is
       made up of multiple lines and sentences.
       This book is written by Md. Mahin Ahmed and Meherab Ahmed
       Both are Graduated from Aust""")

name ="Assalamualaikum Meherab!"
print(name)
print (name[0])
print (name [2:5])
print (name [2:])
print (name*2)
print (name + "How are you?")

listname= ['Md.Mahin Ahmed',2024,7,26,'Meherab', 999.9]
sublist = [720,'Mostafizur Ahmed']
print (listname)
print (listname[0])
print (listname [1:3])
print (listname[2:])
print(sublist*2)
print (listname + sublist)
sublist[0] ='Fatema'
print (sublist)

str = "Mahin Ahmed "
ch = str [5]
print (ch)
print (str[0:11])
print (str[:11]) #[0:11]
print (str[0:]) #[len(str)]
print (str[-13:-1]) #Nagative index

# Code of Function's
str = "i'm a new Coder of python."
print(str.endswith("er."))
print(str.capitalize())
print(str.find("a"))
print(str.count("o"))

a=20
b=10
c=15
d=5
e=0
e = (a+b)*c/d
print ("Value of (a+b)*c/d is ", e )
e =((a+b)*c)/d
print ("Value of ((a+b)*c ) /d is",e )
e = (a+b)*(c/d);
print (" Value of (a+b)* (c/d) is", e)
e = a+(b*c) / d;
print ("VAlue of a+(b*c)/d is",e)

 #Code of strings
str = " Hi, $Iam a doller symbol$ of 99.9$"
print(str.count("$"))
print("str")

# Code of traffic lights

light = input("light colour : ")

if ( light == "red"):
    print("stop")

elif ( light == " yellow "):
     print("look")

elif( light == "green"):
    print("go")

else:
    print("light is broken")

 # code of simple interest

p = float(input ("p : "))
r = float (input ("r"))
t = float (input ("t"))
si = (p*r*t)/100
print(si)

age = 21
if( age >= 18):
    print("can vote")
    print( " Can Drive" )

    # Marks of Exam
marks = 76 

# Determine the grade based on the marks

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("Grade of the student ->", grade)

 #Gather Numbers

a = int(input("Enter a value of a= "))
b = int(input("Enter a value of b= "))
c = int(input("Enter a value of c= "))

if( a>b and b>c ):
    print( "A in a large number")

elif ( b>a and b>c):
    print("B in a large number")

else:
    print(" C in a large number")
 #Triangle Maths
import math
a = int(input( "Enter a value of a ="))
b = int(input( "Enter a value of b ="))
c = int(input( "Enter a value of c ="))

if ( a+b>c and b+c>a and c+a>b ):
    s = (a+b+c)/2
    triangle_area= math.sqrt( s*(s-a)* ( s-b )* ( s-c ))
    print( "triangle area =", triangle_area)

else:
    print( "Triangle area is not possible")

 #RESULT SHEET in PRGMM
 
n = int(input( "Enter a value of n ="))
if ( n>=80 ):
    print( "You got A+")
elif ( n>=75 ):
    print( "You got A- ")
elif ( n>65 ):
    print( " You got B ")
elif ( n>55 ):
    print( " You got C ")
elif ( n> 45 ):
    print( " You got D ")
else:
    print( " You are failed in exams ")

print("Hello World!")

sum = 0
for i in range (1,100,2):
    sum= sum+i*i
    print("Sum in result= ", sum)

sum = 0
for i in range (1,11,2):
    sum= sum+i
    print("Sum in result= ", sum)

a=20
b=10
c=15
d=5
e=0
e = (a+b)*c/d
print ("Value of (a+b)*c/d is ", e )
e =((a+b)*c)/d
print ("Value of ((a+b)*c ) /d is",e )
e = (a+b)*(c/d);
print (" Value of (a+b)* (c/d) is", e)
e = a+(b*c) / d;
print ("VAlue of a+(b*c)/d is",e)
          
#Nasted loop
count = 1
for i in range(10):
    for j in range(0,i):
        print(count, end="")
        count=count+1
    print()
input()

b=0
while b <= 2:
    x=0
    print(b)
    while x <= 2:
        print(x)
        x+=1
    b+=1
    # Nasted While loop statement
    i=2
while (i < 20):
    j=2
    while (j <= (i/j)):
        if not (i % j):
            break
        j = j + 1
    if (j > i/j):
        print (i, "is prime")
    i = i + 1

# 1 to 100 sum of the series devide by 7
n = 100
total_sum = 0
for i in range(7, n + 1, 7):
    total_sum += i
    
print(total_sum)

#ax**2+bx+c=0
import math
p=int(input("Enter the value of p :"))
q=int(input("Enter the value of q :"))
r=int(input("Enter the value of r :"))
d=q**2-4*p*r
if (d==0):
    x1=(-q/(2*p))
    x2=x1;
    print("Roots are real and the values are :")
    print("x1=",x1)
    print("x2=",x2)
elif (d>0):
    x1=((-q+math.sqrt(d))/(2*p))
    x2=((-q-math.sqrt(d))/(2*p))
    print("Roots are real and the values are :")
    print("x1=",x1)
    print("x2=",x2)
else: 
    print("Roots are imaginary!")
    
#extra
n=int(input("Enter the value of n :"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)
    
#1+2+3+...+10
    sum = 0
for i in range(1, 11):
    sum += i
    print("Final sum result =", sum)

#1+2+3+...+n
n=int(input("Enter a value of n="))
sum = 0
for i in range(1,n + 1):
    sum += i
    print("sum result =", sum)
    
#1^2+2^2+3^2+...+10^2
sum = 0
for i in range(1, 11):  
    sum += i**2  
    print("sum of squares =", sum)
    
# Starts at 1, ends at 100, increments by 7
sum = 0
for i in range(1, 101, 7):  
    sum += i
print("sum result =", sum)

# Starts at 2, ends at 10, increments by 2
sum = 0
for i in range(2, 11, 2): 
    sum += i
print("sum result =", sum)

# Starts at 1, ends at 50, increments by 2
sum = 0
for i in range(1, 51, 2):  
    sum += i
print("Final sum result =", sum)

#fibonaci programm in py.
def fibonaci(n):
    f0=1
    f1=2
    for i in range(1,10):
        fibo=f0+f1
        f0=f1
        f1=fibo
        print(fibo,"is a fibo number")
fibo=0
fibonaci(10)

# File read, write and append
file = open("E:\\Mahin\\mahin\\New folder\\mahin.txt", 'w')
file.write('Bangladesh')
file = open("E:\\Mahin\\mahin\\New folder\\mahin.txt", 'a')
file.write(' is my country')
file.close()
file = open("E:\\Mahin\\mahin\\New folder\\mahin.txt", 'r')
x=file.read()
print(x)

# Circle area program
r=float(input("Enter the value of r :"))
Pi=3.1416
circlearea=Pi*r*r
print("The area of circle is:",circlearea)

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

#Generator program...
def sq_numbers(n):
    for i in range(1,n+1):
        yield i*i
a=sq_numbers(4)
print("The square of numbers 1,2,3 are:")
print(next(a))
print(next(a))
print(next(a))

#Decorator program...
def my_decorator(func):                                                 
    def decorate():
        print("-------")
        func()
        print("-------")
    return decorate
def print_raw():
    print("BAngladesh")
decorated_function=my_decorator(print_raw)
decorated_function()
#Decorator program...shct
def my_decorator(func):
    def decorate():
        print("-------")
        func()
        print("-------")
    return decorate

@my_decorator
def print_raw():
    print("BAngladesh")

print_raw()
#Decorator program...also
def decorator (func):
    def decorator_func():
        print("-------")
        func()
        print("-------")
    return decorator_func
def iter_func():
    print("BAngladesh")
decorator_3 = decorator(iter_func)
decorator_3()

# working procedure of itator>>>
a =[0,5,10,14,20]
for i in  a:
    if i%2==0:
        print(str(i) + " is even number")
    else:
        print(str(i) + " is odd number")