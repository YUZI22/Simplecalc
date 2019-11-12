import os
import sys


while True: 
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Remainder")
    print("7.Prcnt")

    def add (x, y):
        return x + y

    def subtract (x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x ,y):
        return x / y

    def power(x, y):
        return x ** y

    def remainder(x, y):
        return x % y

    def prcnt(x, y):
        return x * y / 100 

    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    if len(choice) > 1:
        print ("Only one character is allowed.")
        break

    if choice > '7.': # (REFER TO TAG 1) : Seeing if this would work ( something to compare to )
        print ("Invalid Input")
        answer = input('Run again? (y/n): ')
        if answer == ('y'):
            continue
        if answer == ('n'):
            sys.exit()

    if choice == '123456':
        print ("Invalid Input")
        answer = input('Run again? (y/n): ')
        if answer == ('y'):
            continue
        if answer == ('n'):
            sys.exit()

    if choice == '4321, 3214, 4132, 3234, 3423':
        print ("Invalid Input")
        answer = input('Run again? (y/n): ')
        if answer == ('y'):
            continue
        if answer == ('n'):
            break
        
             
    num1 = float((input("Enter first number: "))) # Got rid of float() before input UPDATE: you NEED to add float to change it to a decimal number!, earlier without float it would do for example, 12+12 without float would be 1212 but with float it would be 24.0
    num2 = float((input("Enter second number: "))) # Got rid of float() before input 
    if choice == "1": # Changed single speech mark to double.
        print(num1,"+",num2,"=", add(num1,num2))
    elif choice == "2": # Changed single speech mark to double.
        print(num1,"-",num2,"=", subtract(num1,num2))
    elif choice == "3": # Changed single speech mark to double.
        print(num1,"*",num2,"=", multiply(num1,num2))
    elif choice == "4": # Changed single speech mark to double.
        print(num1,"/",num2,"=", divide(num1,num2))
    elif choice == "5": # Changed single speech mark to double.
        print(num1,"**",num2,"=", power(num1,num2))
    elif choice == "6": # Changed single speech mark to double.
        print(num1,"%",num2,"=", remainder(num1,num2))
    elif choice == "7":
        print(num1,"%",num2,"=","%", prcnt(num1,num2))
    else:
        print("Invalid Input")


