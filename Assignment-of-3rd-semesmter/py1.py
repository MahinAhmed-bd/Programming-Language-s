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
