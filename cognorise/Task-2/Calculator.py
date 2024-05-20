import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero"
    else:
        return x / y

def perform_calculation():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == 'Addition (+)':
        result.set(add(num1, num2))
    elif operation == 'Subtraction (-)':
        result.set(subtract(num1, num2))
    elif operation == 'Multiplication (*)':
        result.set(multiply(num1, num2))
    elif operation == 'Division (/)':
        result.set(divide(num1, num2))

root = tk.Tk()
root.title("Simple Calculator")

# Set the window size
window_width = 600
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Create a frame to hold the content
content_frame = tk.Frame(root)
content_frame.place(relx=0.5, rely=0.5, anchor="center")

# Define font
font = ("Arial", 16)

# Create entry fields
entry1_label = tk.Label(content_frame, text="Enter first number:", font=font)
entry1_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry1 = tk.Entry(content_frame, font=font)
entry1.grid(row=0, column=1, padx=10, pady=5)

entry2_label = tk.Label(content_frame, text="Enter second number:", font=font)
entry2_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry2 = tk.Entry(content_frame, font=font)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Create operation dropdown
operation_var = tk.StringVar()
operation_var.set("Addition (+)")  # Default operation
operation_label = tk.Label(content_frame, text="Select operation:", font=font)
operation_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
operation_menu = tk.OptionMenu(content_frame, operation_var, "Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)")
operation_menu.grid(row=2, column=1, padx=10, pady=5)

# Create button to perform calculation
calculate_button = tk.Button(content_frame, text="Calculate", command=perform_calculation, font=font)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Create result label
result_label = tk.Label(content_frame, text="Result:", font=font)
result_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
result = tk.StringVar()
result_entry = tk.Entry(content_frame, textvariable=result, state='readonly', font=font)
result_entry.grid(row=4, column=1, padx=10, pady=5)

root.mainloop()
