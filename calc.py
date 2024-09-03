import tkinter as Tkinter
calculation = ""
def Calculation(sym):
    global calculation
    calculation = calculation + str(sym)
    textbox.delete(1.0, "end")
    textbox.insert(1.0, calculation)
    

def eval_calc():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        textbox.delete(1.0, "end")
        textbox.insert(1.0, result)
    except:
        clear_field()
        textbox.insert(1.0, "error")

def clear_field():
    global calculation
    calculation=""
    textbox.delete(1.0, "end")

def calc_percentage():
    global calculation
    try:
        result = str(eval(calculation) / 100)
        calculation = result
        textbox.delete(1.0, "end")
        textbox.insert(1.0, result)
    except:
        clear_field()
        textbox.insert(1.0, "error")

    
root = Tkinter.Tk()
root.geometry("294x340")
root.configure(bg="black")

textbox = Tkinter.Text(root, height=2, width=15, font=("Arial", 24))
textbox.grid(columnspan=5, padx=10, pady=10)

btn1 = Tkinter.Button(root, text="1", bg="grey", command=lambda: Calculation(1),width=5, font=("Arial", 14))
btn1.grid(row=3, column=1, padx=5, pady=10)
btn2 = Tkinter.Button(root, text="2", bg="grey", command=lambda: Calculation(2),width=5, font=("Arial", 14))
btn2.grid(row=3, column=2)
btn3 = Tkinter.Button(root, text="3", bg="grey", command=lambda: Calculation(3),width=5, font=("Arial", 14))
btn3.grid(row=3, column=3)
btn4 = Tkinter.Button(root, text="4", bg="grey", command=lambda: Calculation(4),width=5, font=("Arial", 14))
btn4.grid(row=4, column=1)
btn5 = Tkinter.Button(root, text="5", bg="grey", command=lambda: Calculation(5),width=5, font=("Arial", 14))
btn5.grid(row=4, column=2)
btn6 = Tkinter.Button(root, text="6", bg="grey", command=lambda: Calculation(6),width=5, font=("Arial", 14))
btn6.grid(row=4, column=3)
btn7 = Tkinter.Button(root, text="7", bg="grey", command=lambda: Calculation(7),width=5, font=("Arial", 14))
btn7.grid(row=5, column=1, padx=5, pady=10)
btn8 = Tkinter.Button(root, text="8", bg="grey", command=lambda: Calculation(8),width=5, font=("Arial", 14))
btn8.grid(row=5, column=2)
btn9 = Tkinter.Button(root, text="9", bg="grey", command=lambda: Calculation(9),width=5, font=("Arial", 14))
btn9.grid(row=5, column=3)
btn0 = Tkinter.Button(root, text="0", bg="grey", command=lambda: Calculation(0),width=5, font=("Arial", 14))
btn0.grid(row=6, column=2)

btn_plus = Tkinter.Button(root, text="+", bg="blue", fg="white", command=lambda: Calculation("+"),width=4, font=("Arial", 14))
btn_plus.grid(row=3, column=4)
btn_minus = Tkinter.Button(root, text="-", bg="blue", fg="white", command=lambda: Calculation("-"),width=4, font=("Arial", 14))
btn_minus.grid(row=4, column=4)
btn_mul = Tkinter.Button(root, text="*", bg="blue", fg="white", command=lambda: Calculation("*"),width=4, font=("Arial", 14))
btn_mul.grid(row=5, column=4)
btn_div = Tkinter.Button(root, text="/", bg="blue", fg="white", command=lambda: Calculation("/"),width=4, font=("Arial", 14))
btn_div.grid(row=2, column=4)
btn_open = Tkinter.Button(root, text="(", bg="grey", command=lambda: Calculation("("),width=5, font=("Arial", 14))
btn_open.grid(row=6, column=1)
btn_close = Tkinter.Button(root, text=")", bg="grey", command=lambda: Calculation(")"),width=5, font=("Arial", 14))
btn_close.grid(row=6, column=3)
btn_clear = Tkinter.Button(root, text="C", bg="red", fg="white", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=2, column=3)
btn_equals = Tkinter.Button(root, text="=", bg="green", fg="white", command=eval_calc,width=5, font=("Arial", 14))
btn_equals.grid(row=6, column=4)
btn_dot = Tkinter.Button(root, text=".", bg="blue", fg="white",command=lambda: Calculation("."), width=5, font=("Arial", 14))
btn_dot.grid(row=2, column=1)
btn_percent = Tkinter.Button(root, text="%", bg="blue", fg="white",command=calc_percentage, width=5, font=("Arial", 14))
btn_percent.grid(row=2, column=2)

root.mainloop()