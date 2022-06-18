#this file is used to test classes
#my first commit
#my second commit
#test PC
#this line is added in github

class Student():
    def __init__(self,name,cin,age):
        self.name=name
        self.cin=cin
        self.age=age
    
    def __str__(self):
        return f"name = {self.name}, cin = {self.cin}, the age = {self.age}"
    
    def __eq__(self, other) -> bool:
        return self.cin+self.age == other.cin + other.age
    
    def __bool__(self):
        return self.age>18

class menu():
    def __init__(self,plat,price):
        self.palt=plat
        self.price=price
    
       
    
M1=menu('Milk',20)  
M2=menu("Coffee",80) 
if M1:
    print(f"the price of {M1.palt} is grater than 50 $")
if M2:
        print(f"the price of {M2.palt} is grater than 50 $")

    
Hicham=Student("hicham",123456,35)
adnan=Student("Adnan",123456,35)
print(Hicham)
print(adnan)
print(Hicham==adnan)
if Hicham:
    print("over 18")