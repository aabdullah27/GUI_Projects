# Creating a Simple Calculator
from tkinter import *

# Create the main window
root = Tk()
root.geometry("315x490")  # Set window size
root.title("Simple Calculator")  # Set window title

# Creating Entry Box to take input
e = Entry(root, width=22, borderwidth=5, font=('Arial', 18))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions
def button_action(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
     first_number = e.get()
     global f_num
     global math 
     math = "addition" 
     f_num = int(first_number)
     e.delete(0, END)

def button_equal():
     second_number = e.get()
     e.delete(0, END)
     if math == 'addition':
               e.insert(0 , f_num + int(second_number))
     elif math == 'subtraction':
                e.insert(0 , f_num - int(second_number))
     elif math == 'multiplication':
                e.insert(0 , f_num * int(second_number))
     elif math == 'division':
                 e.insert(0 , f_num / int(second_number))

def button_sub():
     first_number = e.get()
     global f_num
     global math 
     math = "subtraction" 
     f_num = int(first_number)
     e.delete(0, END)

def button_mult():
     first_number = e.get()
     global f_num
     global math 
     math = "multiplication" 
     f_num = int(first_number)
     e.delete(0, END)

def button_div():
     first_number = e.get()
     global f_num
     global math 
     math = "division" 
     f_num = int(first_number)
     e.delete(0, END)

     
# Creating Buttons
b_1 = Button(root,  padx = 40, pady = 30, bg = 'grey', fg = 'white', text = '1', command= lambda: button_action(1))
b_2 = Button(root,  padx = 40, pady = 30, bg = 'grey', fg = 'white', text = '2', command= lambda: button_action(2))
b_3 = Button(root,  padx = 40, pady = 30, bg = 'grey', fg = 'white', text = '3', command= lambda: button_action(3))
b_4 = Button(root,  padx = 40, pady = 30, bg = 'grey', fg = 'white', text = '4', command= lambda: button_action(4))
b_5 = Button(root,  padx = 40, pady = 30, bg = 'grey', fg = 'white', text = '5', command= lambda: button_action(5))
b_6 = Button(root,  padx = 40, pady = 30, bg = 'grey', fg = 'white', text = '6', command= lambda: button_action(6))
b_7 = Button(root,  padx = 40, pady = 30, bg = 'grey', fg = 'white', text = '7', command= lambda: button_action(7))
b_8 = Button(root,  padx = 40, pady = 30, bg = 'grey', fg = 'white', text = '8', command= lambda: button_action(8))
b_9 = Button(root,  padx = 40, pady = 30, bg = 'grey', fg = 'white', text = '9', command= lambda: button_action(9))
b_0 = Button(root,  padx = 40, pady = 30, bg = 'grey', fg = 'white', text = '0', command= lambda: button_action(0))
b_equals = Button(root,  padx = 37, pady = 26, bg = 'grey', fg = 'white', text = '=', font= 'bold', command= button_equal)
b_clear = Button(root,  padx = 73, pady = 30 , bg = 'grey', fg = 'white', text = 'CLEAR', command= button_clear)

b_plus = Button(root,  padx = 36, pady = 4, bg = 'grey', fg = 'white', text = '+', font= 'bold', command= button_add)
b_sub = Button(root,  padx = 38, pady = 6, bg = 'grey', fg = 'white', text = '-', font= 'bold', command= button_sub)
b_mult = Button(root,  padx = 37, pady = 6, bg = 'grey', fg = 'white', text = '*', font= 'bold', command= button_mult)
b_div = Button(root,  padx = 38, pady = 4, bg = 'grey', fg = 'white', text = '/', font= 'bold', command= button_div)

# Placing Buttons on screen
b_1.place(x= 7, y= 55)
b_2.place(x= 103, y= 55)
b_3.place(x= 200, y= 55)

b_4.place(x= 7, y= 142)
b_5.place(x= 103, y= 142)
b_6.place(x= 200, y= 142)

b_7.place(x= 7, y= 227)
b_8.place(x= 103, y= 227)
b_9.place(x= 200, y= 227)

b_0.place(x= 7, y= 312)
b_plus.place(x= 7, y= 442)
b_equals.place(x= 200, y= 398)
b_clear.place(x= 105, y= 312)
b_sub.place(x= 7, y= 398)
b_mult.place(x= 103, y= 398)
b_div.place(x= 103, y= 442)

if __name__ == '__main__':
	root.mainloop()
