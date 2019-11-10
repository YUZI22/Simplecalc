import os
import sys


while True: 
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    def add (x, y):
        return x + y

    def subtract (x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x ,y):
        return x / y

    choice = input("Enter choice(1/2/3/4): ")

    if len(choice) > 1:
        print ("Only one character is allowed.")
        break

    if choice > '4.': # (REFER TO TAG 1) : Seeing if this would work ( something to compare to )
        print ("Invalid Input")
        answer = input('Run again? (y/n): ')
        if answer == ('y'):
            continue
        if answer == ('n'):
            sys.exit()

    if choice == '1234':
        print ("Invalid Input")
        answer = input('Run again? (y/n): ')
        if answer == ('y'):
            continue
        if answer == ('n'):
            sys.exit()

    if choice == '4321, 3214, 4132, 3234, 3423':
        print ("Invalid Input")
        answer = input('Run again? (y/n): ')
        if answer -- ('y'):
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
    else:
        print("Invalid Input")

# nvm just made it end the script when 2 characters are detected.
# how len works: https://www.geeksforgeeks.org/python-string-length-len/ reads the contents of a string or variable in len 
# added only 1 character allowed prompt at "select operation" credit: https://stackoverflow.com/questions/12955495/raw-input-should-accept-only-single-character
#Thinking of making it so that the user can do: add num + num instead of having to select add etc..
#added the . infront of the 4 at line 26 to change it to a float to accept higher number, and also accept numbers that are decimals (floats).
#indentation is very important had to change the entire piece of code.
#DONE WHILE TRUE has to be at the top to start the questions again: refer to my ques: https://stackoverflow.com/questions/58790686/trying-to-make-a-loop-that-stops-on-user-input
# TAG 1 Right now trying to make it so that if the choice is more than 4 it will say invalid input.
# TAG 1 DONE!!!, found out you need to put it right after the (Choice) variable, right now it does not stop the script after the user has done an invalid input.
# TAG 1 Got the method for while from this website: https://en.wikibooks.org/wiki/Python_Programming/Conditional_Statements
# Python operands https://www.tutorialspoint.com/python/comparison_operators_example.htm
# search what def means and what elif means.
# Used this for the calc code: https://www.programiz.com/python-programming/examples/calculator also (Calculator.py has the actual file) 
# Used this website for floating point https://www.google.com/search?client=firefox-b-d&q=how+does+float+input+mean+in+python

