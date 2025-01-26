from tkinter import *
import base64
from tkinter import messagebox


# Function to encrypt the message
def encrypt_message():
    try:
        message = text_input.get("1.0", END).strip()  # Get and strip input
        key = key_input.get().strip()  # Get key and strip

        if not key or not message:
            messagebox.showerror("Error", "Message and Key cannot be empty!")
            return

        # Concatenate message and key
        combined_message = message + key
        encoded_bytes = base64.b64encode(combined_message.encode("utf-8"))
        encrypted_message = encoded_bytes.decode("utf-8")  # Convert bytes to string

        result_output.delete(0, END)
        result_output.insert(0, encrypted_message)  # Show encrypted message
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during encryption: {str(e)}")


# Function to decrypt the message
def decrypt_message():
    try:
        encrypted_text = text_input.get("1.0", END).strip()  # Get and strip input
        key = key_input.get().strip()  # Get key and strip

        if not key or not encrypted_text:
            messagebox.showerror("Error", "Encrypted text and Key cannot be empty!")
            return

        # Decode the encrypted message
        decoded_bytes = base64.b64decode(encrypted_text)
        decoded_message = decoded_bytes.decode("utf-8")

        # Check if key matches at the end
        if decoded_message.endswith(key):
            original_message = decoded_message[:-len(key)]  # Remove key from end
            result_output.delete(0, END)
            result_output.insert(0, original_message)  # Show decrypted message
        else:
            messagebox.showerror("Decryption Error", "Decryption failed. Incorrect key.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during decryption: {str(e)}")


# Function to clear all inputs and output
def clear_fields():
    text_input.delete("1.0", END)
    key_input.delete(0, END)
    result_output.delete(0, END)


# Tkinter GUI setup
root = Tk()
root.geometry("500x400")
root.title("Secret Communication Tool")

# Input for message
Label(root, text="Enter your Message:", font=("Helvetica", 12)).pack(pady=5)
text_input = Text(root, height=5, width=50)
text_input.pack(pady=5)

# Input for key
Label(root, text="Enter Encryption Key:", font=("Helvetica", 12)).pack(pady=5)
key_input = Entry(root, show="*", width=50)
key_input.pack(pady=5)

# Buttons
Button(root, text="Encrypt", command=encrypt_message, bg="lightblue", font=("Helvetica", 12)).pack(pady=10)
Button(root, text="Decrypt", command=decrypt_message, bg="lightgreen", font=("Helvetica", 12)).pack(pady=10)
Button(root, text="Clear", command=clear_fields, bg="lightcoral", font=("Helvetica", 12)).pack(pady=10)

# Result display
Label(root, text="Output (Copyable):", font=("Helvetica", 12)).pack(pady=5)
result_output = Entry(root, font=("Helvetica", 12), width=50)
result_output.pack(pady=5)

root.mainloop()
