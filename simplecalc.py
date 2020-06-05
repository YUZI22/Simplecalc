"""
You can also add multiline comments like these at the start of a script. I would always add these comments, to write things like:
	- name of the program
	- version of the program
	- author(s)
	- (possibly a description of what the program is supposed to do)
	- Date the program was created (idk when you started this so I can't add it myself)
	- Date the program was last edited

(btw fyi if you don't know what "N/A" means: It means "Not Applicable")

Name: Simplecalc
Version: 1.0.14
Authors: Jaron Frerichs <https://github.com/IntelliRon>, Yusef Aslam <https://github.com/YUZI22>
Date created: N/A
Date edited: 05/06/2020


Btw: The code I wrote may look a little different in some editors, since I used Notepad++ at the start, and used TAB instead of four spaces
Also. I just added some comments where I fixed errors. You don't always have to do that. Only add comments where necessary (for example to describe what a function does)
"""

# Function to add two numbers
def add(a, b):
    return a + b


# Function to subtract the second number from the first
def subtract(a, b):
    return a - b


# Function to divide the first number by the second number
def divide(a, b):
    return a / b


# I renamed the multiply method from times. Of course I also changed all the words and the calls to this method
# Function to multiply two numbers
def multiply(a, b):
    return a * b


# Function to take the first number to the power of the second number
def power(a, b):
    return a ** b


# Function to get a percentage of two numbers
def prcnt(a, b):
        return a * b / 100


# Function to get the remainder when dividing the first number by the second number
def remainder(a, b):
        return a % b


# Remember to add whitespace to keep your code tidy. Also add comments like I am currently doing, to explain what the code does
# Function to request operation mode for user
def selectop():
    print ("Select an operation:")
    selectop = input("Manual define mode (MD)/Automatic define mode (AD): ")
    # Program literally just exited when someone entered something different, other than an uppercase MD or AD
    # Program now gives 'error' and then shuts down, and people can enter in whatever case they want
    if selectop.upper() == str("MD"):
        test()
    elif selectop.upper() == str("AD"):
        options()
    else:
        print ("Invalid Operation. Shutting down...")
        shutdown()


# Function with automatic operation mode (no manual selector)
def options():
    while True:
        print ("Select operation:\n")
        print ("1. Add")
        print ("2. Subtract")
        print ("3. Divide")
        print ("4. Multiply")
        print ("5. Power")
        print ("6. Percentage of")
        print ("7. Remainder of")
        print ("8. Off\n")
        
        # Changed string in input from "Type here (1/2/3/4/5/6/7/8): " to "Type here (1-8): "
        opselect = input("Type here (1-8): ")
        if opselect == "8":
           shutdown()
           break
        # Moved a and b up here to check for errors (removed repetitive code)
        firstnum = input("Enter your first number here: ")
        secndnum = input("Enter your second number here: ")
        a = 0
        b = 0
        try:
            a = float(firstnum)
            b = float(scndnum)
        except ValueError:
            print ("Error. At least one of the two numbers are not a number!")
            continue
        # You didn't need the brackets around the checks (eg. opselect == ("1") was not necessary. Instead opselect == "1")
        # Selection mode: Add
        if opselect == "1":
            print (a, "+", b, "=", add(a, b))
        # Selection mode: Subtract
        elif opselect == "2": 
            print (a, "-", b, "=", subtract(a, b))
        # Selection mode: Divide
        elif opselect == "3":
            print (a, "÷", b, "=", divide(a, b))
        # Selection mode: Multiply
        elif opselect == "4":
            print (a, "*", b, "=", multiply(a, b))
        # Selection mode: Power
        elif opselect == "5":
            print (a, "^", b, "=", power(a, b))
        # Selection mode: Percentage
        elif opselect == "6":
            print (a, "% of", b, "=", prcnt(a, b))
        # Selection mode: Remainder
        elif opselect == "7":
            print (a, "remainder of", b, "=", remainder(a, b))
        else:
            print ("Invalid Input.")


# Function with manual operation mode (user has to manually select which operator they are going to use, instead of selecting by number
def test():
    while True:
        mathop = input("Math Operator add(+), subtract(-), divide(/), multiply(*), powerof(^), prcnt(*/), remainder(%), Off(off): ")
        if mathop == "off":
            shutdown()
            break
        firstnum = input("1st num: ")
        secndnum = input("2nd num: ")
        # Do "try-except" statement to prevent errors when casting from String to float
        try:
            a = float(firstnum)
            b = float(secndnum)
        except ValueError:
            print ("Error. At least one of the two numbers are not a number!")
            continue
        # Check for operator used.
        # Operation mode: Add
        if mathop == str("+"):
            print (a, mathop, b, "=", add(a, b))
        # Operation mode: Subtract
        # WARNING: There was an error here where the numbers were added instead of getting subtracted
        elif mathop == str("-"):
            print (a, mathop, b, "=", subtract(a, b))
        # Operation mode: Divide
        elif mathop == str("/"):
            print (a, mathop, b, "=", divide(a, b))
        # Operation mode: Multiply
        elif mathop == str("*"):
            print (a, mathop, b, "=", multiply(a, b))
        # Operation mode: Power
        elif mathop == str("^"):
            print (a, mathop, b, "=", power(a, b))
        # Operation mode: Percentage
        elif mathop == str("*/"):
            print (a, mathop, b, "=", prcnt(a, b))
        # Operation mode: Remainder
        elif mathop == str("%"):
            print (a, mathop, b, "=", remainder(a, b))
        else:
            print("Invalid Math Operator.")


# Function to shutdown program
def shutdown():
	print("Calculator is shutting down...")
	print("Shutdown Complete. Goodbye")
	raise SystemExit


# Print Header
print ("""+-+-+-+-+-+-+-+-+-+-+
|C|a|l|c|u|l|a|t|o|r| 
+-+-+-+-+-+-+-+-+-+-+""")
print ("""
+-+-+-+-+-+-+-+-+
|v|.|1|.|0|.|1|4|
+-+-+-+-+-+-+-+-+""")

# Main program Function call
selectop()
