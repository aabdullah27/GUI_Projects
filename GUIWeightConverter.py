from tkinter import *

# Function to perform weight conversion
def convert_weight():
    weight_type = weight_type_entry.get().lower()
    weight_value = float(weight_input_entry.get())
    
    if weight_type == 'pounds':
        converted_weight = weight_value * 0.453592  # Pounds to kilograms
        result_label.config(text=f"{weight_value} pounds is {converted_weight:.2f} kilograms")
    elif weight_type == 'kilograms':
        converted_weight = weight_value * 2.20462  # Kilograms to pounds
        result_label.config(text=f"{weight_value} kilograms is {converted_weight:.2f} pounds")
    else:
        result_label.config(text="Unsupported weight type. Use 'pounds' or 'kilograms'.")

# Setting up the main window
root = Tk()
root.geometry('450x300')  # Adjusting size of window
root.title('Weight Converter')  # Setting the title

# Creating labels and entry boxes
label_1 = Label(root, text='Enter the weight type (pounds/kilograms): ', font=('Arial', 12))
label_1.place(x=50, y=20)

weight_type_entry = Entry(root, width=22, borderwidth=5, font=('Arial', 12))
weight_type_entry.place(x=50, y=50)

label_2 = Label(root, text='Enter the weight value: ', font=('Arial', 12))
label_2.place(x=50, y=100)

weight_input_entry = Entry(root, width=22, borderwidth=5, font=('Arial', 12))
weight_input_entry.place(x=50, y=130)

# Creating the conversion button
convert_button = Button(root, text="Convert", command=convert_weight, font=('Arial', 12))
convert_button.place(x=180, y=180)

# Label to display the result
result_label = Label(root, text='', font=('Arial', 12))
result_label.place(x=50, y=230)

if __name__ == '__main__':
    root.mainloop()
