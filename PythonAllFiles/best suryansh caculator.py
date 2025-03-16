import tkinter as tk
from tkinter import messagebox
import math

# Global memory storage
memory = 0

# Button click function
def on_click(button_text):
    current_text = entry_var.get()

    try:
        if button_text == "C":
            entry_var.set("")
        elif button_text == "CE":
            entry_var.set(current_text[:-1])
        elif button_text == "=":
            result = eval(current_text, {"__builtins__": None}, {"math": math})
            entry_var.set(result)
        elif button_text == "√":
            entry_var.set(math.sqrt(float(current_text)))
        elif button_text == "x²":
            entry_var.set(float(current_text) ** 2)
        elif button_text == "1/x":
            entry_var.set(1 / float(current_text))
        elif button_text in ["sin", "cos", "tan", "log"]:
            num = float(current_text)
            if button_text == "sin":
                entry_var.set(math.sin(math.radians(num)))
            elif button_text == "cos":
                entry_var.set(math.cos(math.radians(num)))
            elif button_text == "tan":
                entry_var.set(math.tan(math.radians(num)))
            elif button_text == "log":
                entry_var.set(math.log10(num))
        elif button_text == "M+":
            global memory
            memory += float(current_text)
        elif button_text == "M-":
            memory -= float(current_text)
        elif button_text == "MR":
            entry_var.set(memory)
        elif button_text == "MC":
            memory = 0
        else:
            entry_var.set(current_text + button_text)
    except:
        messagebox.showerror("Error", "Invalid Input")

# GUI Setup
root = tk.Tk()
root.title("Suryansh - Calculator")
root.geometry("320x450")
root.configure(bg="black")

# Add GUI Banner
title_label = tk.Label(root, text="SURYANSH - CALCULATOR", font=("Arial", 16, "bold"), bg="black", fg="white")
title_label.pack(fill="both")

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="both")

# Button Layout
buttons = [
    ["MC", "MR", "M+", "M-"],
    ["CE", "C", "√", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "x²", "="],
    ["sin", "cos", "tan", "log"]
]

for row in buttons:
    frame = tk.Frame(root, bg="black")
    frame.pack(fill="both", expand=True)
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font=("Arial", 14), width=5, height=2,
                           command=lambda text=btn_text: on_click(text))
        button.pack(side="left", expand=True)

root.mainloop()