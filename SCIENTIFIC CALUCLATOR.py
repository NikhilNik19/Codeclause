import tkinter as tk
import tkinter.messagebox
from math import sqrt, sin, cos, tan, radians

window = tk.Tk()
window.title("NIKHIL's Calculator")

frame = tk.Frame(master=window, bg="Grey", padx=10)
frame.pack()

entry = tk.Entry(master=frame, relief=tk.SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


def calculate_result():
    try:
        expression = entry.get()
        if "sin" in expression:
            result = sin(get_angle(expression))  # Evaluate sin function
        elif "cos" in expression:
            result = cos(get_angle(expression))  # Evaluate cos function
        elif "tan" in expression:
            result = tan(get_angle(expression))  # Evaluate tan function
        elif "sqrt" in expression:
            result = sqrt(get_argument(expression))  # Evaluate square root
        else:
            result = eval(expression)  # Evaluate other expressions

        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        tkinter.messagebox.showinfo("Error", str(e))


def clear_entry():
    entry.delete(0, tk.END)


def get_angle(expression):
    angle_str = expression[expression.index('(') + 1:expression.index(')')]
    angle = float(angle_str)
    return radians(angle)


def get_argument(expression):
    argument_str = expression[expression.index('(') + 1:expression.index(')')]
    return float(argument_str)


button_1 = tk.Button(master=frame, text='1', padx=15, pady=5, width=5, command=lambda: button_click(1))
button_1.grid(row=1, column=0, pady=2)

button_2 = tk.Button(master=frame, text='2', padx=15, pady=5, width=5, command=lambda: button_click(2))
button_2.grid(row=1, column=1, pady=2)

button_3 = tk.Button(master=frame, text='3', padx=15, pady=5, width=5, command=lambda: button_click(3))
button_3.grid(row=1, column=2, pady=2)

button_plus = tk.Button(master=frame, text='+', padx=15, pady=5, width=5, command=lambda: button_click('+'))
button_plus.grid(row=1, column=3, pady=2)

button_4 = tk.Button(master=frame, text='4', padx=15, pady=5, width=5, command=lambda: button_click(4))
button_4.grid(row=2, column=0, pady=2)

button_5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=5, command=lambda: button_click(5))
button_5.grid(row=2, column=1, pady=2)

button_6 = tk.Button(master=frame, text='6', padx=15, pady=5, width=5, command=lambda: button_click(6))
button_6.grid(row=2, column=2, pady=2)

button_minus = tk.Button(master=frame, text='-', padx=15, pady=5, width=5, command=lambda: button_click('-'))
button_minus.grid(row=2, column=3, pady=2)

button_7 = tk.Button(master=frame, text='7', padx=15, pady=5, width=5, command=lambda: button_click(7))
button_7.grid(row=3, column=0, pady=2)

button_8 = tk.Button(master=frame, text='8', padx=15, pady=5, width=5, command=lambda: button_click(8))
button_8.grid(row=3, column=1, pady=2)

button_9 = tk.Button(master=frame, text='9', padx=15, pady=5, width=5, command=lambda: button_click(9))
button_9.grid(row=3, column=2, pady=2)

button_multiply = tk.Button(master=frame, text='*', padx=15, pady=5, width=5, command=lambda: button_click('*'))
button_multiply.grid(row=3, column=3, pady=2)

button_decimal = tk.Button(master=frame, text='.', padx=15, pady=5, width=5, command=lambda: button_click('.'))
button_decimal.grid(row=4, column=1, pady=2)

button_bracket_open = tk.Button(master=frame, text='(', padx=15, pady=5, width=5, command=lambda: button_click('('))
button_bracket_open.grid(row=4, column=2, pady=2)

button_bracket_close = tk.Button(master=frame, text=')', padx=15, pady=5, width=5, command=lambda: button_click(')'))
button_bracket_close.grid(row=4, column=3, pady=2)




button_0 = tk.Button(master=frame, text='0', padx=15, pady=5, width=5, command=lambda: button_click(0))
button_0.grid(row=4, column=0, pady=2)





button_cos = tk.Button(master=frame, text='cos', padx=15, pady=5, width=5, command=lambda: button_click('cos('))
button_cos.grid(row=5, column=1, pady=2)

button_tan = tk.Button(master=frame, text='tan', padx=15, pady=5, width=5, command=lambda: button_click('tan('))
button_tan.grid(row=5, column=2, pady=2)

button_divide = tk.Button(master=frame, text='/', padx=15, pady=5, width=5, command=lambda: button_click('/'))
button_divide.grid(row=5, column=3, pady=2)

button_sin = tk.Button(master=frame, text='sin', padx=15, pady=5, width=5, command=lambda: button_click('sin('))
button_sin.grid(row=5, column=0, pady=2)


button_clear = tk.Button(master=frame, text="Clear", padx=15, pady=5, width=11, command=clear_entry)
button_clear.grid(row=6, column=0, pady=2, columnspan=2)

button_equals = tk.Button(master=frame, text="=", padx=15, pady=5, width=11, command=calculate_result)
button_equals.grid(row=6, column=2, pady=2, columnspan=2)

window.mainloop()
