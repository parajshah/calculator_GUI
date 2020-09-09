from tkinter import *
import math

expression = ""

def press(num):
    global expression
    expression += str(num)
    eqn.set(expression)

def clear_expression():
    global expression
    expression = ""
    eqn.set(expression)

def square():
    global expression
    try:
        total = str(eval(expression) ** 2)
        expression = total
        eqn.set(total)
    except:
        eqn.set("Cannot find square of empty or incomplete expression!")
        expression  = ""

def square_root():
    global expression
    try:
        total = str(math.sqrt(eval(expression)))
        expression = total
        eqn.set(total)
    except:
        eqn.set("Cannot perform squareroot on empty or incomplete expression!")
        expression  = ""

def reciprocal():
    global expression
    try:
        total = str(1 / eval(expression))
        expression = total
        eqn.set(total)
    except:
        eqn.set("Cannot perform reciprocal on empty or incomplete expression!")
        expression  = ""
    

def press_equal():
    global expression
    try:
        total = str(eval(expression))
        eqn.set(total)
        expression = total
    except:
        eqn.set("Error occured!")
        expression = ""


window = Tk()
window.title("Calculator")
##window.configure(bg = "orange")

eqn = StringVar()

expression_field = Label(window, textvariable = eqn, width = 50)
expression_field.grid(columnspan = 4, ipadx = 20, ipady = 5)

# Numbers

button9 = Button(window, text = "9", command = lambda: press(9), height = 3, width = 12)
button9.grid(row = 2, column = 2)
button8 = Button(window, text = "8", command = lambda: press(8), height = 3, width = 12)
button8.grid(row = 2, column = 1)
button7 = Button(window, text = "7", command = lambda: press(7), height = 3, width = 12)
button7.grid(row = 2, column = 0)
button6 = Button(window, text = "6", command = lambda: press(6), height = 3, width = 12)
button6.grid(row = 3, column = 2)
button5 = Button(window, text = "5", command = lambda: press(5), height = 3, width = 12)
button5.grid(row = 3, column = 1)
button4 = Button(window, text = "4", command = lambda: press(4), height = 3, width = 12)
button4.grid(row = 3, column = 0)
button3 = Button(window, text = "3", command = lambda: press(3), height = 3, width = 12)
button3.grid(row = 4, column = 2)
button2 = Button(window, text = "2", command = lambda: press(2), height = 3, width = 12)
button2.grid(row = 4, column = 1)
button1 = Button(window, text = "1", command = lambda: press(1), height = 3, width = 12)
button1.grid(row = 4, column = 0)
button0 = Button(window, text = "0", command = lambda: press(0), height = 3, width = 12)
button0.grid(row = 5, column = 0)

# Operations

onebyx = Button(window, text = "1/x", command = reciprocal, height = 3, width = 12)
onebyx.grid(row = 1, column = 0)
square = Button(window, text = "x**2", command = square, height = 3, width = 12)
square.grid(row = 1, column = 1)
squareroot = Button(window, text = "sqrt(x)", command = square_root, height = 3, width = 12)
squareroot.grid(row = 1, column = 2)
plus = Button(window, text = "+", command = lambda: press("+"), height = 3, width = 12)
plus.grid(row = 1, column = 3)
minus = Button(window, text = "-", command = lambda: press("-"), height = 3, width = 12)
minus.grid(row = 2, column = 3)
multiply = Button(window, text = "x", command = lambda: press("*"), height = 3, width = 12)
multiply.grid(row = 3, column = 3)
divide = Button(window, text = "/", command = lambda: press("/"), height = 3, width = 12)
divide.grid(row = 4, column = 3)
equal = Button(window, text = "=", command = press_equal, height = 3, width = 12)
equal.grid(row = 5, column = 3)
decimal = Button(window, text = ".", command = lambda: press("."), height = 3, width = 12)
decimal.grid(row = 5, column = 1)
clear = Button(window, text = "Clear", command = clear_expression, height = 3, width = 12)
clear.grid(row = 5, column = 2)

window.mainloop()
