
# Practices 1
A = int (input("A : " ))
G = input( " M/F : ")

if((A == 1 or A== 2) and G == "M"):
    print("fee is 100")

elif( A == 3 or A == 4 or G == "F"):
    print(" fee is 200")

elif( A == 5 or G == "M"):
    print("fee is 300")

else:
    print("no fee")

    #Arithmic operators
a = 7
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #reminder
print(a ** b) #a^b
    
    #Relational Operators
a = 30
b = 50

print( a == b )
print( a != b )
print( a >= b )
print( a > b )
print( a <= b )
print( a < b)

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


