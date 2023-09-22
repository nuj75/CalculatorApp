import tkinter as tk

window = tk.Tk()
window.columnconfigure([0,1,2],weight=2,minsize=60)
window.rowconfigure([6],weight=2, minsize=100)



textNumberOne = 0
textNumberTwo = 0
global operatorBool
operatorBool = False
currentOperation = ""
equalsBool = False

def addNum(num):
    global operatorBool
    global equalsBool

    if equalsBool:
        clear()
        equalsBool = False

    if(operatorBool):
        global textNumberTwo
        textNumberTwo = textNumberTwo*10 + num
        global numberTwo 
        numberTwo.config(text=textNumberTwo)
    else:
        global textNumberOne
        textNumberOne = textNumberOne*10 + num
        global numberOne
        numberOne.config(text=textNumberOne)


def addOperation(theOperation):
    global equalsBool
    global textNumberOne
    global numberOne
    
    if equalsBool:
        result = numberTwo.cget("text")
        clear()
        textNumberOne = result
        numberOne.config(text=textNumberOne)
        equalsBool = False
    
    global operation
    operation.config(text=theOperation)
    
    global operatorBool
    operatorBool = True
    global currentOperation
    currentOperation = theOperation

def equal():
    global currentOperation
    global textNumberOne
    global textNumberTwo
    global operationBool 

    

    operationBool = True

    result = 0
    if currentOperation == "+":
        result = textNumberTwo + textNumberOne
    elif currentOperation == "-":
        result = textNumberOne - textNumberTwo
    elif currentOperation == "*":
        result = textNumberOne * textNumberTwo
    elif currentOperation == "/":
        result = textNumberOne/textNumberTwo

    
    global numberTwo

    clear()

    global equalsBool
    equalsBool=True

    numberTwo.config(text=result)
    


        



def clear():
    global textNumberOne
    textNumberOne = 0
    global textNumberTwo
    textNumberTwo = 0
    global operatorBool
    operatorBool = False
    global currentOperation
    currentOperation = ""
    numberOne.config(text="")
    numberTwo.config(text="")
    operation.config(text="")
    


frameDisplay = tk.Frame(
    bg="Blue",
    height=75,
    width=300
)

numberOne = tk.Label(
    master=frameDisplay,
    text="",
    bg="Grey",
    fg="Black",
    width=6,
    height=2
)
numberOne.config(font=('Helvatical bold',30, 'bold', 'italic'))
numberOne.grid(row = 1, column=0)

operation = tk.Label(
    master=frameDisplay,
    text="",
    bg="Grey",
    fg="Black",
    width=2,
    height=2
)
operation.config(font=('Helvatical bold',30, 'bold', 'italic'))
operation.grid(row = 1, column=1)

numberTwo = tk.Label(
    master=frameDisplay,
    text="",
    bg="Grey",
    fg="Black",
    width=6,
    height=2
)
numberTwo.config(font=('Helvatical bold',30, 'bold', 'italic'))
numberTwo.grid(row = 1, column=2)

frameDisplay.grid(row = 1, column= 1, sticky="n")
frameDisplay.grid_propagate(0)



frameOne = tk.Frame(
    bg="Blue",
    height=75,
    width=300
)

ONE = tk.Button(
    master=frameOne,
    text="1",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addNum(1)
)
ONE.config(font=('Helvatical bold',30, 'bold', 'italic'))
ONE.grid(row = 2, column=0)

TWO = tk.Button(
    master=frameOne,
    text="2",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addNum(2)
)
TWO.config(font=('Helvatical bold',30, 'bold', 'italic'))
TWO.grid(row = 2, column=1)

THREE = tk.Button(
    master=frameOne,
    text="3",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addNum(3)
)
THREE.config(font=('Helvatical bold',30, 'bold', 'italic'))
THREE.grid(row = 2, column=2)

PLUS = tk.Button(
    master=frameOne,
    text="+",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addOperation("+")
)
PLUS.config(font=('Helvatical bold',30, 'bold', 'italic'))
PLUS.grid(row = 2, column=3)


frameOne.grid(row = 2, column= 1)
frameOne.grid_propagate(0)



frameTwo = tk.Frame(
    bg="Blue",
    height=75,
    width=300
)

FOUR = tk.Button(
    master=frameTwo,
    text="4",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addNum(4)
)
FOUR.config(font=('Helvatical bold',30, 'bold', 'italic'))
FOUR.grid(row = 3, column=0)

FIVE = tk.Button(
    master=frameTwo,
    text="5",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addNum(5)
)
FIVE.config(font=('Helvatical bold',30, 'bold', 'italic'))
FIVE.grid(row = 3, column=1)

SIX = tk.Button(
    master=frameTwo,
    text="6",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addNum(6)
)
SIX.config(font=('Helvatical bold',30, 'bold', 'italic'))
SIX.grid(row = 3, column=2)

MINUS = tk.Button(
    master=frameTwo,
    text="-",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addOperation("-")
    
)
MINUS.config(font=('Helvatical bold',30, 'bold', 'italic'))
MINUS.grid(row = 3, column=3)


frameTwo.grid(row = 3, column= 1)
frameTwo.grid_propagate(0)



frameThree = tk.Frame(
    bg="Blue",
    height=75,
    width=300
)

SEVEN = tk.Button(
    master=frameThree,
    text="7",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addNum(7)
)
SEVEN.config(font=('Helvatical bold',30, 'bold', 'italic'))
SEVEN.grid(row = 4, column=0)

EIGHT = tk.Button(
    master=frameThree,
    text="8",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addNum(8)
)
EIGHT.config(font=('Helvatical bold',30, 'bold', 'italic'))
EIGHT.grid(row = 4, column=1)

NINE = tk.Button(
    master=frameThree,
    text="9",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addNum(9)
)
NINE.config(font=('Helvatical bold',30, 'bold', 'italic'))
NINE.grid(row = 4, column=2)

MULT = tk.Button(
    master=frameThree,
    text="*",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addOperation("*")
)
MULT.config(font=('Helvatical bold',30, 'bold', 'italic'))
MULT.grid(row = 4, column=3)


frameThree.grid(row = 4, column= 1)
frameThree.grid_propagate(0)

frameFour = tk.Frame(
    bg="Blue",
    height=75,
    width=300
)

ZERO = tk.Button(
    master=frameFour,
    text="0",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addNum(0)
)
ZERO.config(font=('Helvatical bold',30, 'bold', 'italic'))
ZERO.grid(row = 5, column=0)

DIV = tk.Button(
    master=frameFour,
    text="/",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    command=lambda: addOperation("/")
)
DIV.config(font=('Helvatical bold',30, 'bold', 'italic'))
DIV.grid(row = 5, column=1)

EQUALS = tk.Button(
    master=frameFour,
    command=equal,
    text="=",
    bg="Grey",
    fg="Black",
    width=2,
    height=2
)
EQUALS.config(font=('Helvatical bold',30, 'bold', 'italic'))
EQUALS.grid(row = 5, column=2)

CLEAR = tk.Button(
    master=frameFour,
    command=clear,
    text="C",
    bg="Grey",
    fg="Black",
    width=2,
    height=2,
    font=('Helvatical bold',30, 'bold', 'italic')
)

CLEAR.grid(row=5, column=3)




frameFour.grid(row = 5, column= 1)
frameFour.grid_propagate(0)

window.mainloop()