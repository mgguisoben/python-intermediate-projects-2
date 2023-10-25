import tkinter as tk
from tkinter import *


def convert():
    x = float(num.get())
    x_unit = unit_1.get()
    y_unit = unit_2.get()

    meter_x = METER_CONVERSIONS[x_unit](x)
    y = METER_CONVERSIONS[y_unit](meter_x)

    output.config(text=f"{y:.3f}")


METER_CONVERSIONS = {
    'Mile': lambda i: i * 1609.344,
    'Yard': lambda i: i * 0.9144,
    'Feet': lambda i: i * 0.3048,
    'Inch': lambda i: i * 0.0254,
    'Kilometer': lambda i: i * 1000,
    'Meter': lambda i: i,
    'Centimeter': lambda i: i * 0.01,
    'Millimeter': lambda i: i * 0.001
}

UNITS = [unit for unit in METER_CONVERSIONS.keys()]
FONT = ('Arial', 15, 'normal')

window = tk.Tk()
window.title("Length Converter")
window.minsize()
window.config(padx=20, pady=20)

unit_1 = StringVar(window, value=UNITS[0])
unit_2 = StringVar(window, value=UNITS[1])

num = tk.StringVar(window, value='0.0')

entry = tk.Entry(window, textvariable=num)
entry.config(font=FONT)
entry.grid(column=1, row=0)

option_1 = tk.OptionMenu(window, unit_1, *UNITS)
option_1.config(font=FONT, padx=5)
option_1.grid(column=2, row=0)

option_2 = tk.OptionMenu(window, unit_2, *UNITS)
option_2.config(font=FONT, padx=5, )
option_2.grid(column=2, row=1)

button = tk.Button(text="Convert", command=convert, font=FONT)
button.config(padx=5)
button.grid(column=1, row=2)

label = tk.Label(text="is equal to: ", font=FONT)
label.grid(column=0, row=1)

output = tk.Label(text=0.0, font=FONT)
output.grid(column=1, row=1)

window.mainloop()
