import tkinter as tk

calc = " "

def add_to_calc(symbol):
    global calc
    calc += str(symbol)
    text_results.delete(1.0, "end")
    text_results.insert(1.0, calc)

def evalute_calc():
    global calc
    try:
        calc = str(eval(calc))
        text_results.delete(1.0, "end")
        text_results.insert(1.0, calc)
    except:
       clear_field()
       text_results.insert(1.0, "Error")

def clear_field():
    global calc
    calc = ""
    text_results.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")

text_results = tk.Text(root, height = 2, width = 16, font =("Arial", 24))
text_results.grid(columnspan = 5)

# BUTTONS
button_1 = tk.Button(root, text = "1", command = lambda: add_to_calc(1), width = 5, font = ("Arial", 14))
button_1.grid(row = 2, column = 1)

button_2 = tk.Button(root, text = "2", command = lambda: add_to_calc(2), width = 5, font = ("Arial", 14))
button_2.grid(row = 2, column = 2)

button_3 = tk.Button(root, text = "3", command = lambda: add_to_calc(3), width = 5, font = ("Arial", 14))
button_3.grid(row = 2, column = 3)

button_4 = tk.Button(root, text = "4", command = lambda: add_to_calc(4), width = 5, font = ("Arial", 14))
button_4.grid(row = 3, column = 1)

button_5 = tk.Button(root, text = "5", command = lambda: add_to_calc(5), width = 5, font = ("Arial", 14))
button_5.grid(row = 3, column = 2)

button_6 = tk.Button(root, text = "6", command = lambda: add_to_calc(6), width = 5, font = ("Arial", 14))
button_6.grid(row = 3, column = 3)

button_7 = tk.Button(root, text = "7", command = lambda: add_to_calc(7), width = 5, font = ("Arial", 14))
button_7.grid(row = 4, column = 1)

button_8 = tk.Button(root, text = "8", command = lambda: add_to_calc(8), width = 5, font = ("Arial", 14))
button_8.grid(row = 4, column = 2)

button_9 = tk.Button(root, text = "9", command = lambda: add_to_calc(9), width = 5, font = ("Arial", 14))
button_9.grid(row = 4, column = 3)

button_0 = tk.Button(root, text = "0", command = lambda: add_to_calc(0), width = 5, font = ("Arial", 14))
button_0.grid(row = 5, column = 2)

#SYMBOL FUNCTIONS ( +, -,...)
button_plus = tk.Button(root, text = "+", command = lambda: add_to_calc("+"), width = 5, font = ("Arial", 14))
button_plus.grid(row = 2, column = 4)

button_subtraction = tk.Button(root, text = "-", command = lambda: add_to_calc("-"), width = 5, font = ("Arial", 14))
button_subtraction.grid(row = 3, column = 4)

button_multiplication = tk.Button(root, text = "x", command = lambda: add_to_calc("x"), width = 5, font = ("Arial", 14))
button_multiplication.grid(row = 4, column = 4)

button_division = tk.Button(root, text = "/", command = lambda: add_to_calc("/"), width = 5, font = ("Arial", 14))
button_division.grid(row = 5, column = 4)

button_left_parenthesis = tk.Button(root, text = "(", command = lambda: add_to_calc("("), width = 5, font = ("Arial", 14))
button_left_parenthesis.grid(row = 5, column = 1)

button_right_parenthesis = tk.Button(root, text = ")", command = lambda: add_to_calc(")"), width = 5, font = ("Arial", 14))
button_right_parenthesis.grid(row = 5, column = 3)

button_plus = tk.Button(root, text = "+", command = lambda: add_to_calc("+"), width = 5, font = ("Arial", 14))
button_plus.grid(row = 2, column = 4)

button_equal = tk.Button(root, text = "=", command = evalute_calc, width = 11, font = ("Arial", 14))
button_equal.grid(row = 6, column = 3, columnspan = 2)

button_clear = tk.Button(root, text = "clear", command = clear_field, width = 11, font = ("Arial", 14))
button_clear.grid(row = 6, column = 1, columnspan = 2)

root.mainloop()