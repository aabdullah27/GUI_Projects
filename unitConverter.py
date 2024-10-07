import tkinter as tk
from tkinter import ttk

# Conversion functions for different categories
def length_to_si(unit, value):
    # Convert length units to meters (SI unit for length)
    conversion_factors = {'centimeter': 0.01, 'meter': 1, 'kilometer': 1000, 'inch': 0.0254, 'foot': 0.3048}
    return value * conversion_factors[unit]

def weight_to_si(unit, value):
    # Convert weight units to kilograms (SI unit for weight)
    conversion_factors = {'gram': 0.001, 'kilogram': 1, 'pound': 0.453592, 'ounce': 0.0283495}
    return value * conversion_factors[unit]

def temperature_to_si(unit, value):
    # Convert temperature units to Kelvin (SI unit for temperature)
    if unit == 'Celsius':
        return value + 273.15
    elif unit == 'Fahrenheit':
        return (value - 32) * 5 / 9 + 273.15
    else:
        return value  # Assuming input in Kelvin

def volume_to_si(unit, value):
    # Convert volume units to cubic meters (SI unit for volume)
    conversion_factors = {'milliliter': 1e-6, 'liter': 1e-3, 'cubic meter': 1, 'gallon': 0.00378541}
    return value * conversion_factors[unit]

# Convert function for the button
def convert():
    value = float(entry_value.get())
    unit = unit_var.get()
    category = category_var.get()

    if category == "Length":
        result = length_to_si(unit, value)
        result_label.config(text=f"{result:.4f} meters")
    elif category == "Weight":
        result = weight_to_si(unit, value)
        result_label.config(text=f"{result:.4f} kilograms")
    elif category == "Temperature":
        result = temperature_to_si(unit, value)
        result_label.config(text=f"{result:.2f} Kelvin")
    elif category == "Volume":
        result = volume_to_si(unit, value)
        result_label.config(text=f"{result:.4f} cubic meters")
    else:
        result_label.config(text="Invalid Category")


# Create the main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")

# Use ttk for fancy widgets
style = ttk.Style()
style.theme_use('clam')

# Category Dropdown
category_var = tk.StringVar()
category_label = ttk.Label(root, text="Select Category:")
category_label.pack(pady=10)

category_dropdown = ttk.Combobox(root, textvariable=category_var, values=["Length", "Weight", "Temperature", "Volume"],
                                 state="readonly")
category_dropdown.pack()

# Unit Dropdown
unit_var = tk.StringVar()
unit_label = ttk.Label(root, text="Select Unit:")
unit_label.pack(pady=10)

unit_dropdown = ttk.Combobox(root, textvariable=unit_var, state="readonly")
unit_dropdown.pack()

# Input Value
entry_value = tk.StringVar()
entry_label = ttk.Label(root, text="Enter Value:")
entry_label.pack(pady=10)

entry_box = ttk.Entry(root, textvariable=entry_value)
entry_box.pack()

# Bind category selection to update unit options
def update_units(event):
    category = category_var.get()
    if category == "Length":
        unit_dropdown.config(values=["centimeter", "meter", "kilometer", "inch", "foot"])
    elif category == "Weight":
        unit_dropdown.config(values=["gram", "kilogram", "pound", "ounce"])
    elif category == "Temperature":
        unit_dropdown.config(values=["Celsius", "Fahrenheit", "Kelvin"])
    elif category == "Volume":
        unit_dropdown.config(values=["milliliter", "liter", "cubic meter", "gallon"])

category_dropdown.bind("<<ComboboxSelected>>", update_units)

# Conversion Button
convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

# Result Label
result_label = ttk.Label(root, text="", font=('Arial', 14))
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
