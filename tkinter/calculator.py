import tkinter as tk

# Function to update expression
def press(key):
    if key == "+/-":
        current = entry_var.get()
        if current:
            if current[0] == "-":
                entry_var.set(current[1:])
            else:
                entry_var.set("-" + current)
    else:
        entry_var.set(entry_var.get() + str(key))

# Function to evaluate the expression
def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the entry field
def clear():
    entry_var.set("")

# Creating main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x500")
root.configure(bg="white")

# StringVar to hold input/output
entry_var = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=10, relief="ridge", justify="right", bg="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=20, sticky="nsew")

# Buttons layout
buttons = [
    ('AC', 1, 0), ('()', 1, 1), ('%', 1, 2), ('÷', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),
]

# Color settings for specific buttons
button_colors = {
    "AC": {"bg": "gray", "fg": "white"},
    "=": {"bg": "orange", "fg": "white"},
    "+": {"bg": "orange", "fg": "black"},
    "-": {"bg": "orange", "fg": "black"},
    "×": {"bg": "orange", "fg": "black"},
    "÷": {"bg": "orange", "fg": "black"},
    "%": {"bg": "gray", "fg": "black"},
    "()": {"bg": "gray", "fg": "black"},
    "+/-": {"bg": "orange", "fg": "black"},
}

# Creating buttons
for (text, row, col) in buttons:
    if text == "AC":
        action = clear
    elif text == "=":
        action = calculate
    elif text == "÷":
        action = lambda x="/": press(x)
    elif text == "×":
        action = lambda x="*": press(x)
    else:
        action = lambda x=text: press(x)
    
    # Apply colors from `button_colors` if available
    btn_config = button_colors.get(text, {"bg": "white", "fg": "black"})
    
    btn = tk.Button(root, text=text, font=("Arial", 20), command=action, height=2, width=6, 
                    bg=btn_config["bg"], fg=btn_config["fg"])
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run Tkinter event loop
root.mainloop()
