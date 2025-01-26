import random
import string
from tkinter import *

# Function to generate the password
def generate_password():
    try:
        length = int(length_input.get())  # Get the desired password length
    except ValueError:
        result_display.delete(0, END)
        result_display.insert(0, "Invalid length!")  # Show error if length is not a number
        return

    include_uppercase = uppercase_var.get()  # Check if uppercase is selected
    include_lowercase = lowercase_var.get()  # Check if lowercase is selected
    include_numbers = numbers_var.get()  # Check if numbers are selected
    include_symbols = symbols_var.get()  # Check if symbols are selected

    # Build the character pool based on selected options
    char_pool = ''
    if include_uppercase:
        char_pool += string.ascii_uppercase
    if include_lowercase:
        char_pool += string.ascii_lowercase
    if include_numbers:
        char_pool += string.digits
    if include_symbols:
        char_pool += string.punctuation

    # Ensure at least one character type is selected
    if not char_pool:
        result_display.delete(0, END)
        result_display.insert(0, "Select at least one option!")  # Show error if no options are selected
        return

    # Generate the password by randomly picking characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))

    # Display the generated password
    result_display.delete(0, END)  # Clear the previous result
    result_display.insert(0, password)  # Insert the new password

# Setting up the main Tkinter window
root = Tk()
root.title("Password Generator")
root.geometry("400x300")  # You can adjust the window size as needed

# Label for password length input
length_label = Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)

# Entry for the user to input the length of the password
length_input = Entry(root)
length_input.grid(row=0, column=1, padx=10, pady=5)

# Checkboxes for password options
uppercase_var = BooleanVar()
lowercase_var = BooleanVar()
numbers_var = BooleanVar()
symbols_var = BooleanVar()

uppercase_checkbox = Checkbutton(root, text="Include Uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=0, sticky=W, padx=10)

lowercase_checkbox = Checkbutton(root, text="Include Lowercase", variable=lowercase_var)
lowercase_checkbox.grid(row=2, column=0, sticky=W, padx=10)

numbers_checkbox = Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbox.grid(row=3, column=0, sticky=W, padx=10)

symbols_checkbox = Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbox.grid(row=4, column=0, sticky=W, padx=10)

# Button to generate the password
generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Entry to display the generated password
result_display = Entry(root)
result_display.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Run the Tkinter main loop
root.mainloop()
