from tkinter import *
import parser
import math


root = Tk()
root.title('Calculator')
root.geometry('354x320')
root.minsize(354,320)
root.maxsize(354,320)

pos = 0
def get_variables(num):
    global pos
    display.insert(pos,num)
    pos += 1
 
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
 
def get_operation(operator):
    global pos
    length = len(operator)
    display.insert(pos,operator)
    pos += length
 
def clear_all():
    display.delete(0,END)
 
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

def fact():
    entire_string = display.get()
    try:
        result = math.factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

display = Entry(root, font=("Calibri",14),bg="white",fg="black",bd=0)
display.grid(row=1,columnspan=6,sticky=N+E+W+S, ipady = 8)
 
Button(root,text="1",command = lambda :get_variables(1), width = 7, height = 3).grid(row=2,column=0, sticky=N+S+E+W)
Button(root,text="2",command = lambda :get_variables(2), width = 7, height = 3).grid(row=2,column=1, sticky=N+S+E+W)
Button(root,text="3",command = lambda :get_variables(3), width = 7, height = 3).grid(row=2,column=2, sticky=N+S+E+W)
 
Button(root,text="4",command = lambda :get_variables(4), width = 7, height = 3).grid(row=3,column=0, sticky=N+S+E+W)
Button(root,text="5",command = lambda :get_variables(5), width = 7, height = 3).grid(row=3,column=1, sticky=N+S+E+W)
Button(root,text="6",command = lambda :get_variables(6), width = 7, height = 3).grid(row=3,column=2, sticky=N+S+E+W)

Button(root,text="7",command = lambda :get_variables(7), width = 7, height = 3).grid(row=4,column=0, sticky=N+S+E+W)
Button(root,text="8",command = lambda :get_variables(8), width = 7, height = 3).grid(row=4,column=1, sticky=N+S+E+W)
Button(root,text="9",command = lambda :get_variables(9), width = 7, height = 3).grid(row=4,column=2, sticky=N+S+E+W)
 
Button(root,text="AC",command =lambda :clear_all(), width = 7, height = 3).grid(row=5,column=0, sticky=N+S+E+W)
Button(root,text="0",command = lambda :get_variables(0), width = 7, height = 3).grid(row=5,column=1, sticky=N+S+E+W)
Button(root,text=".",command =lambda :get_variables("."), width = 7, height = 3).grid(row=5, column=2, sticky=N+S+E+W)
 
# Basic Operations
Button(root,text="+",command = lambda :get_operation("+"), width = 7, height = 3).grid(row=2,column=3, sticky=N+S+E+W)
Button(root,text="-",command = lambda :get_operation("-"), width = 7, height = 3).grid(row=3,column=3, sticky=N+S+E+W)
Button(root,text="*",command = lambda :get_operation("*"), width = 7, height = 3).grid(row=4,column=3, sticky=N+S+E+W)
Button(root,text="/",command = lambda :get_operation("/"), width = 7, height = 3).grid(row=5,column=3, sticky=N+S+E+W)

Button(root,text="pi",command = lambda :get_operation("*3.14"), width = 7, height = 3).grid(row=2,column=4, sticky=N+S+E+W)
Button(root,text="mod",command = lambda :get_operation("%"), width = 7, height = 3).grid(row=3,column=4, sticky=N+S+E+W)
Button(root,text="(",command = lambda :get_operation("("), width = 7, height = 3).grid(row=4,column=4, sticky=N+S+E+W)
Button(root,text="exp",command = lambda :get_operation("**"), width = 7, height = 3).grid(row=5,column=4, sticky=N+S+E+W)

Button(root,text=u"\u232B",command = lambda :undo(), width = 7, height = 3).grid(row=2,column=5, sticky=N+S+E+W)
Button(root,text="x!", command = lambda: fact(), width = 7, height = 3).grid(row=3,column=5, sticky=N+S+E+W)
Button(root,text=")",command = lambda :get_operation(")"), width = 7, height = 3).grid(row=4,column=5, sticky=N+S+E+W)
Button(root,text="^2",command = lambda :get_operation("**2"), width = 7, height = 3).grid(row=5,column=5, sticky=N+S+E+W)

Button(root,text="=",command = lambda :calculate(), width = 7, height = 3).grid(columnspan=6, sticky=N+S+E+W)
 
root.mainloop()
