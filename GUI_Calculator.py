from tkinter import *

# Create the main window
root = Tk()
root.geometry("350x475")  # Set window size
root.title("Simple Calculator")  # Set window title

# Creating Entry Box to take input
e = Entry(root, width=40, borderwidth=5, font=('Arial', 18))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions
def button_action(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

def clear_action():
    e.delete(0, END)

def calculate_action():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, str(result))
    except Exception as ex:
        e.delete(0, END)
        e.insert(0, "Error")

# Button Definitions
button_params = {'padx': 20, 'pady': 20, 'bg': 'lightgrey', 'fg': 'black', 'font': ('Arial', 14)}

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 0),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('=', 4, 1, 2), ('CLEAR', 5, 0, 4)
]

for (text, row, col, *span) in buttons:
    if text == 'CLEAR':
        Button(root, text=text, command=clear_action, **button_params).grid(row=row, column=col, columnspan=span[0], sticky='nsew')
    elif text == '=':
        Button(root, text=text, command=calculate_action, **button_params).grid(row=row, column=col, columnspan=span[0], sticky='nsew')
    else:
        Button(root, text=text, command=lambda t=text: button_action(t), **button_params).grid(row=row, column=col, columnspan=span[0] if span else 1, sticky='nsew')

# Adjust grid weights to make buttons expand with window resize
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

if __name__ == '__main__':
    root.mainloop()
