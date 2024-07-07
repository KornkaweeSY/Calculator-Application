from tkinter import *


root = Tk()
root.title("Calculator")
root.iconbitmap("icons/cal-logo.ico")
root.geometry("300x400+800+300")
root.resizable(0,0)

def nagative():
    result = float(display.get()) * -1
    
    display.delete(0, END)
    display.insert(0, result)

def square():
    result = float(display.get()) ** 2

    display.delete(0, END)
    display.insert(0, result)

def inverse():
    if display.get() == "0":
        result = "Error"
    else:
        result = 1 / float(display.get())

    display.delete(0, END)
    display.insert(0, result)

def clearDisplay():
    display.delete(0, END)
    enableOpetator()


def showNumber(number):
    display.insert(END, number)
    if "." in display.get():
        btnDecimal.config(state=DISABLED)

def equal():
    if operator == "add":
        result = float(firstNumber) + float(display.get())
    elif operator == "subtrack":
        result = float(firstNumber) - float(display.get())
    elif operator == "multiply":
        result = float(firstNumber) * float(display.get())
    elif operator == "divide":
        if display.get() == "0":
            result = "ERROR"
        else:
            result = float(firstNumber) / float(display.get())
    elif operator == "exponent":
        result = float(firstNumber) ** float(display.get())
    
    display.delete(0, END)
    display.insert(0, result)
    enableOpetator()

def operation(value):
    global firstNumber
    global operator
    operator = value
    firstNumber = display.get()

    #reset state
    btnDecimal.config(state=NORMAL)
    display.delete(0, END)

    #disable operator button
    btnAdd.config(state=DISABLED)
    btnSubtrack.config(state=DISABLED)
    btnMutiply.config(state=DISABLED)
    btnDivide.config(state=DISABLED)
    btnExponent.config(state=DISABLED)
    btnInverse.config(state=DISABLED)
    btnSquare.config(state=DISABLED)

def enableOpetator():
    btnAdd.config(state=NORMAL)
    btnSubtrack.config(state=NORMAL)
    btnMutiply.config(state=NORMAL)
    btnDivide.config(state=NORMAL)
    btnExponent.config(state=NORMAL)
    btnInverse.config(state=NORMAL)
    btnSquare.config(state=NORMAL)
    btnDecimal.config(state=NORMAL)



#setting
color = "orange"
displayFont = ("Arail", 35)
btnFont = ("Arail", 19)

#design frame
displayFrame = LabelFrame(root)
buttonFrame = LabelFrame(root)
displayFrame.pack(padx=2, pady=5)
buttonFrame.pack(pady=2 )

#display frame
display = Entry(displayFrame, width=30, font=displayFont, bg="white", border=5, justify=RIGHT)
display.pack(padx=5, pady=5)

#clear & quit
btnClear = Button(buttonFrame, text="Clear", font=btnFont, command=clearDisplay)
btnQuit = Button(buttonFrame, text="Quit", font=btnFont, command=root.destroy)
btnClear.grid(row=0, column=0, columnspan=2, ipadx=35, sticky="WE")
btnQuit.grid(row=0, column=2, columnspan=2, ipadx=35, sticky="WE")

#operator button
btnInverse = Button(buttonFrame, text="1/x", font=btnFont, bg=color, command=inverse)
btnSquare = Button(buttonFrame, text="x^2", font=btnFont, bg=color, command=square)
btnExponent = Button(buttonFrame, text="x^n", font=btnFont, bg=color, command=lambda:operation("exponent"))
btnDivide = Button(buttonFrame, text="/", font=btnFont, bg=color, command=lambda:operation("divide"))
btnMutiply = Button(buttonFrame, text="x", font=btnFont, bg=color, command=lambda:operation("multiply"))
btnSubtrack = Button(buttonFrame, text="-", font=btnFont, bg=color, command=lambda:operation("subtrack"))
btnAdd = Button(buttonFrame, text="+", font=btnFont, bg=color, command=lambda:operation("add"))
btnEqual = Button(buttonFrame, text="=", font=btnFont, bg=color, command=equal)
btnDecimal = Button(buttonFrame, text=".", font=btnFont, bg=color, command=lambda:showNumber("."))
btnNagative = Button(buttonFrame, text="+/-", font=btnFont, bg=color, command=nagative)

#number button
btn9 = Button(buttonFrame, text="9", font=btnFont, bg="black", fg="white", command=lambda:showNumber(9))
btn8 = Button(buttonFrame, text="8", font=btnFont, bg="black", fg="white", command=lambda:showNumber(8))
btn7 = Button(buttonFrame, text="7", font=btnFont, bg="black", fg="white", command=lambda:showNumber(7))
btn6 = Button(buttonFrame, text="6", font=btnFont, bg="black", fg="white", command=lambda:showNumber(6))
btn5 = Button(buttonFrame, text="5", font=btnFont, bg="black", fg="white", command=lambda:showNumber(5))
btn4 = Button(buttonFrame, text="4", font=btnFont, bg="black", fg="white", command=lambda:showNumber(4))
btn3 = Button(buttonFrame, text="3", font=btnFont, bg="black", fg="white", command=lambda:showNumber(3))
btn2 = Button(buttonFrame, text="2", font=btnFont, bg="black", fg="white", command=lambda:showNumber(2))
btn1 = Button(buttonFrame, text="1", font=btnFont, bg="black", fg="white", command=lambda:showNumber(1))
btn0 = Button(buttonFrame, text="0", font=btnFont, bg="black", fg="white", command=lambda:showNumber(0))

#row1
btnInverse.grid(row=1, column=0, pady=1, ipadx=10, sticky="WE")
btnSquare.grid(row=1, column=1, pady=1, ipadx=10, sticky="WE")
btnExponent.grid(row=1, column=2, pady=1, ipadx=10, sticky="WE")
btnDivide.grid(row=1, column=3, pady=1, ipadx=10, sticky="WE")

#row2
btn7.grid(row=2, column=0, pady=1, ipadx=10, sticky="WE")
btn8.grid(row=2, column=1, pady=1, ipadx=10, sticky="WE")
btn9.grid(row=2, column=2, pady=1, ipadx=10, sticky="WE")
btnMutiply.grid(row=2, column=3, pady=1, ipadx=10, sticky="WE")

#row3
btn4.grid(row=3, column=0, pady=1, ipadx=10, sticky="WE")
btn5.grid(row=3, column=1, pady=1, ipadx=10, sticky="WE")
btn6.grid(row=3, column=2, pady=1, ipadx=10, sticky="WE")
btnSubtrack.grid(row=3, column=3, pady=1, ipadx=10, sticky="WE")

#row4
btn1.grid(row=4, column=0, pady=1, ipadx=10, sticky="WE")
btn2.grid(row=4, column=1, pady=1, ipadx=10, sticky="WE")
btn3.grid(row=4, column=2, pady=1, ipadx=10, sticky="WE")
btnAdd.grid(row=4, column=3, pady=1, ipadx=10, sticky="WE")

#row5
btnNagative.grid(row=5, column=0, pady=1, ipadx=10, sticky="WE")
btn0.grid(row=5, column=1, pady=1, ipadx=10, sticky="WE")
btnDecimal.grid(row=5, column=2, pady=1, ipadx=10, sticky="WE")
btnEqual.grid(row=5, column=3, pady=1, ipadx=10, sticky="WE")


root.mainloop()

