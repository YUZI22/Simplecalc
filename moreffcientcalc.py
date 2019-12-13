def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def divide(a, b):
    return a / b
def times(a, b):
    return a * b
def power(a, b):
    return a ** b
def prcnt(a, b):
        return a * b / 100 
def remainder(a, b):
        return a % b
def options():
    while True:
        print ("Select operation:")
        print()
        print ("1. Add")
        print ("2. Subtract")
        print ("3. Divide")
        print ("4. Times")
        print ("5. Power")
        print ("6. Percentage of")
        print ("7. Remainder of")
        print()
        opselect = input("Type here (1/2/3/4/5/6/7): ")
        if opselect == ("1"):
            firstnum = input("Enter your first number here: ")
            secndnum = input("Enter your second number here: ")
            a = float(firstnum)
            b = float(secndnum)
            print (a, "+", b, "=", add(a, b))
        elif opselect == ("2"): 
            firstnum = input("Enter your first number here: ")
            secndnum = input("Enter your second number here: ")
            a = float(firstnum)
            b = float(secndnum)
            print (a, "-", b, "=", subtract(a, b))
        elif opselect == ("3"):
            firstnum = input("Enter your first number here: ")
            secndnum = input("Enter your second number here: ")
            a = float(firstnum)
            b = float(secndnum)
            print (a, "÷", b, "=", divide(a, b))
        elif opselect == ("4"):
            firstnum = input("Enter your first number here: ")
            secndnum = input("Enter your second number here: ")
            a = float(firstnum)
            b = float(secndnum)
            print (a, "x", b, "=", times(a, b))
        elif opselect == ("5"):
            firstnum = input("Enter your first number here: ")
            secndnum = input("Enter your second number here: ")
            a = float(firstnum)
            b = float(secndnum)
            print (a, "**", b, "=", power(a, b))
        elif opselect == ("6"):
            firstnum = input("Enter your first number here: ")
            secndnum = input("Enter your second number here: ")
            a = float(firstnum)
            b = float(secndnum)
            print (a, "% of", b, "=", prcnt(a, b))
        elif opselect == ("7"):
            firstnum = input("Enter your first number here: ")
            secndnum = input("Enter your second number here: ")
            a = float(firstnum)
            b = float(secndnum)
            print (a, "remainder of", b, "=", remainder(a, b))
        else:
            print ("Invalid Input.")
        break
    
    
       

print ("Calculator v1.0.12")

options()


