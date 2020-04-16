from tkinter import *

def clicked():
	lbl.configure(text="")

def clicked1():
	res = lbl["text"] + "1"
	lbl.configure(text=res)

def clicked2():
	res = lbl["text"] + "2"
	lbl.configure(text=res)

def clicked3():
	res = lbl["text"] + "3"
	lbl.configure(text=res)

def clicked4():
	res = lbl["text"] + "4"
	lbl.configure(text=res)

def clicked5():
	res = lbl["text"] + "5"
	lbl.configure(text=res)

def clicked6():
	res = lbl["text"] + "6"
	lbl.configure(text=res)

def clicked7():
	res = lbl["text"] + "7"
	lbl.configure(text=res)

def clicked8():
	res = lbl["text"] + "8"
	lbl.configure(text=res)

def clicked9():
	res = lbl["text"] + "9"
	lbl.configure(text=res)

def clicked0():
	res = lbl["text"] + "0"
	lbl.configure(text=res)	
	
def clicked_plus():
	res = lbl["text"] + "+"
	lbl.configure(text=res)	
	
def clicked_minus():
	res = lbl["text"] + "-"
	lbl.configure(text=res)

def clicked_multiply():
	res = lbl["text"] + "*"
	lbl.configure(text=res)
	
def clicked_divide():
	res = lbl["text"] + "/"
	lbl.configure(text=res)
	
def clicked_clear():
	lbl.configure(text="")
	

def clicked_equal():
	expression = lbl["text"]
	total = str(eval(expression))
	lbl.configure(text=total)


	
window = Tk()

window.geometry('180x390')

window.title("")

lbl = Label(window, text="", font=("Arial Bold", 30))
lbl.grid(column=0, row=0, columnspan=5)

btn1 = Button(window, text="1", command=clicked1)
btn1.grid(column=1, row=1)
btn1.config(height=5, width=5)

btn2 = Button(window, text="2", command=clicked2)
btn2.grid(column=2, row=1)
btn2.config(height=5, width=5)

btn3 = Button(window, text="3", command=clicked3)
btn3.grid(column=3, row=1)
btn3.config(height=5, width=5)

btn4 = Button(window, text="4", command=clicked4)
btn4.grid(column=1, row=2)
btn4.config(height=5, width=5)

btn5 = Button(window, text="5", command=clicked5)
btn5.grid(column=2, row=2)
btn5.config(height=5, width=5)

btn6 = Button(window, text="6", command=clicked6)
btn6.grid(column=3, row=2)
btn6.config(height=5, width=5)

btn7 = Button(window, text="7", command=clicked7)
btn7.grid(column=1, row=3)
btn7.config(height=5, width=5)

btn8 = Button(window, text="8", command=clicked8)
btn8.grid(column=2, row=3)
btn8.config(height=5, width=5)

btn9 = Button(window, text="9", command=clicked9)
btn9.grid(column=3, row=3)
btn9.config(height=5, width=5)

btn0 = Button(window, text="0", command=clicked0)
btn0.grid(column=2, row=4)
btn0.config(height=5, width=5)

btn_plus = Button(window, text="+", command=clicked_plus)
btn_plus.grid(column=4, row=1)
btn_plus.config(height=5, width=5)

btn_minus = Button(window, text="-", command=clicked_minus)
btn_minus.grid(column=4, row=2)
btn_minus.config(height=5, width=5)

btn_multiply = Button(window, text="x", command=clicked_multiply)
btn_multiply.grid(column=4, row=3)
btn_multiply.config(height=5, width=5)

btn_divide = Button(window, text="/", command=clicked_divide)
btn_divide.grid(column=4, row=4)
btn_divide.config(height=5, width=5)

btn_equal = Button(window, text="=", command=clicked_equal)
btn_equal.grid(column=3, row=4)
btn_equal.config(height=5, width=5)

btn_clear = Button(window, text="C", command=clicked_clear)
btn_clear.grid(column=1, row=4)
btn_clear.config(height=5, width=5)

window.mainloop()
