print("number 1 addition")
print("number 2 substraction")
print("number 3 factor")
print("number 4 devision")
x=1
while x==1:
    choice=int(input("enter here: "))
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    if choice==1:
        print(num1+num2)
    if choice==2:
        print(num1-num2)
    if choice==3:
        print(num1*num2)
    if choice == 4:
        print(num1/num2)
