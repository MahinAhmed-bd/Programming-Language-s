import csv
fname='C:\\3Users\\Shazzad\\Downloads\\SampleCSVFile_556kb.csv'
fruits=[]
n=int(input("How many fruits do you want to enter? :"))#()
for i in range(n):
    name=input(f"Enter name of the fruits #{i+1}:")
    unit_price=int(input("Unit price:"))
    quantity=int(input("Quantity"))
    total=unit_price*quantity
    fruits.append([name,unit_price,quantity,total])
with open(fname,mode='w') as file:
    writer=csv.writer(file)
    writer.writerow(['Fruit Name','unit_price','quantity','total'])
    writer.writerows(fruits)
print('Data saved to csv successfully')
print("The enventory is:")
with open(fname,mode='r') as file:
    reader=csv.reader(file)
    for row in reader :
        print(row)
    
