from tkinter import *
import parser
i = 0


def get_variable(num):
    global i
    textarea.insert(i, num)
    i = i+1


def get_opperator(op):
    global i
    textarea.insert(i, op)
    i = i + len(op)


def calculate():
    entier_string = textarea.get()
    try:
        a = parser.expr(entier_string).compile()
        result = eval(a)
        clearAll()
        textarea.insert(0,result)
    except EXCEPTION:
        clearAll()
        textarea.insert(0, "Error!")


def clearAll():
    textarea.delete(0, END)


def undo():
    s1 = textarea.get()
    if len(s1)!=0:
        s2 = s1[:-1]
        clearAll()
        get_variable(s2)
    else:
        textarea.insert(0, "Error!")

root = Tk()
root.title("My Calculator")
# input area
textarea = Entry(root)
textarea.grid(row=1, columnspan=6, sticky=W + E)
# buttons
Button(root, text="1", command=lambda: get_variable(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_variable(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: get_variable(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: get_variable(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_variable(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_variable(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: get_variable(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_variable(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_variable(9)).grid(row=4, column=2)

Button(root, text="AC", command=lambda: clearAll()).grid(row=5, column=0)
Button(root, text="0", command=lambda: get_variable(0)).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)

Button(root, text="+", command=lambda: get_variable("+")).grid(row=2, column=3)
Button(root, text="(", command=lambda: get_variable("(")).grid(row=3, column=3)
Button(root, text="*", command=lambda: get_variable("*")).grid(row=4, column=3)
Button(root, text="^2", command=lambda: get_variable("**2")).grid(row=5, column=3)

Button(root, text="-", command=lambda: get_variable("-")).grid(row=2, column=4)
Button(root, text=")", command=lambda: get_variable(")")).grid(row=3, column=4)
Button(root, text="/", command=lambda: get_variable("/")).grid(row=4, column=4)
Button(root, text="root(2)", command=lambda: get_variable("*1.41")).grid(row=5, column=4)

Button(root, text="C", command=lambda: undo()).grid(row=2, column=5)
Button(root, text="exp", command=lambda: get_variable("**")).grid(row=3, column=5)
Button(root, text="pi", command=lambda: get_variable("*3.14")).grid(row=4, column=5)
Button(root, text="%", command=lambda: get_variable("%")).grid(row=5, column=5)
root.mainloop()
