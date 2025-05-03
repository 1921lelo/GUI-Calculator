#importing required libraries
import tkinter as tk

#initial empty string
calc = " "

#function to add
def addToCalc(symbol):
    global calc
    calc += str(symbol)
    textResult.delete(1.0, "end") #clears the text box
    textResult.insert(1.0, calc) #inserts the new string

#function to evaluate the expression
def evaluateCalc():
    global calc
    try:
        result = str(eval(calc)) #evaluates expression safely
        calc = result
        textResult.delete(1.0, "end") #clears evaluated expression
        textResult. insert(1.0, calc) #inserts new expression for evaluation
    except:
        clearCalc()
        textResult.insert(1.0, "Error") #returns an error if the expression is invalid
        

def clearCalc():
    global calc
    calc =""
    textResult.delete(1.0, "end")

#build basic GUI/ window for calculator
root = tk.Tk()
root.geometry("300x275")
root.title("Calculator")

#text display for calculator
textResult = tk.Text(root, height=2, width=16, font=("Noto Sans",24))
textResult.grid(columnspan=5)

#digit controls
btn1 = tk.Button(root, text="1", command = lambda: addToCalc(1), width="5", font=("Noto Sans", 14))
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command = lambda: addToCalc(2), width="5", font=("Noto Sans", 14))
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command = lambda: addToCalc(3), width="5", font=("Noto Sans", 14))
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command = lambda: addToCalc(4), width="5", font=("Noto Sans", 14))
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command = lambda: addToCalc(5), width="5", font=("Noto Sans", 14))
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command = lambda: addToCalc(6), width="5", font=("Noto Sans", 14))
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command = lambda: addToCalc(7), width="5", font=("Noto Sans", 14))
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command = lambda: addToCalc(8), width="5", font=("Noto Sans", 14))
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command = lambda: addToCalc(9), width="5", font=("Noto Sans", 14))
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command = lambda: addToCalc(0), width="5", font=("Noto Sans", 14))
btn0.grid(row=5, column=2)

#operator controls
btnPlus = tk.Button(root, text="+", command = lambda: addToCalc("+"), width="5", font=("Noto Sans", 14))
btnPlus.grid(row=2, column=4)
btnMinus = tk.Button(root, text="-", command = lambda: addToCalc("-"), width="5", font=("Noto Sans", 14))
btnMinus.grid(row=3, column=4)
btnMultiply = tk.Button(root, text="*", command = lambda: addToCalc("*"), width="5", font=("Noto Sans", 14))
btnMultiply.grid(row=4, column=4)
btnDivide = tk.Button(root, text="/", command = lambda: addToCalc("/"), width="5", font=("Noto Sans", 14))
btnDivide.grid(row=5, column=4)

#parentheses controls
btnOpen = tk.Button(root, text="(", command = lambda: addToCalc("("), width="5", font=("Noto Sans", 14))
btnOpen.grid(row=5, column=1)
btnShut = tk.Button(root, text=")", command = lambda: addToCalc(")"), width="5", font=("Noto Sans", 14))
btnShut.grid(row=5, column=3)

#clear and equals controls
btnClear = tk.Button(root, text="C", command = clearCalc, width="11", font=("Noto Sans", 14))
btnClear.grid(row=6, column=1, columnspan=2)
btnEquals = tk.Button(root, text="=", command = evaluateCalc, width="11", font=("Noto Sans", 14))
btnEquals.grid(row=6, column=3, columnspan=2)


#starts main loop for GUI
root.mainloop()

