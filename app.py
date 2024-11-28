import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import importlib
import os

# Updated modules
modules = {
    "1-RSA": ("solution_1_encode", "solution_1_decode"),
    "2-Permutation": ("solution_2_encode", "solution_2_decode"),
    "3-Quot": ("solution_3_encode", "solution_3_decode"),
    "4-lettercase": ("solution_4_encode", "solution_4_decode"),
    "5-space": ("solution_5_encode", "solution_5_decode"),
    "project_1": ("projekt_solution_1_encode", "projekt_solution_1_decode"),
    "project_2": ("projekt_solution_2_encode", "projekt_solution_2_decode")
}

def open_html_file():
    file_path = filedialog.askopenfilename(
        title="Choose HTML or CSS file",
        filetypes=[("HTML files", "*.html"), ("CSS files", "*.css")]
    )
    return file_path

def run_encode(module_name, message_text, output_text):
    html_path = open_html_file()
    if not html_path:
        return

    try:
        with open(html_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Import encoding module
        encode_module = importlib.import_module(module_name)
        
        # Get the message from the input text box
        message = message_text.get("1.0", tk.END).strip()
        
        if not message:
            messagebox.showerror("ERROR", "Enter your message!")
            return
        
        # Encode the message
        modified_html = encode_module.process_html(html_content, message)
        
        output_file_path = os.path.join(os.path.dirname(html_path), f"output.{html_path.split(sep='.')[-1]}")
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(modified_html)
        
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Encoded HTML saved to: {output_file_path}")
    
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"Failed to encode the file: {e}")

def run_decode(module_name, output_text):
    html_path = open_html_file()
    if not html_path:
        return

    try:
        with open(html_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Import decoding module
        decode_module = importlib.import_module(module_name)
        
        # Decode the message
        decoded_message = decode_module.extract_password(html_content)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Decoded Message: {decoded_message}")
    
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"Failed to decode the file: {e}")

# main
root = tk.Tk()
root.title("Steganography App")
# root.state('zoomed')  # Start maximized

frame = ttk.Frame(root)
frame.pack(expand=True, fill="both", padx=10, pady=10)

from help import HELP_TEXT
help_button = tk.Button(frame, text="Help", command=lambda: messagebox.showinfo("Help", HELP_TEXT))
help_button.pack(pady=5)

# Encoding section
encode_label = tk.Label(frame, text="Encode a Message", font=('Arial', 14))
encode_label.pack(pady=10)

message_text = tk.Text(frame, height=10, width=100)
message_text.pack(pady=5)

encode_output_text = tk.Text(frame, height=5, width=100)
encode_output_text.pack(pady=5)

encode_button = tk.Button(frame, text="Encode and Save", command=lambda: run_encode(modules[selected_module.get()][0], message_text, encode_output_text))
encode_button.pack(pady=5)

# Decoding section
decode_label = tk.Label(frame, text="Decode a Message", font=('Arial', 14))
decode_label.pack(pady=10)

decode_output_text = tk.Text(frame, height=5, width=100)
decode_output_text.pack(pady=5)

decode_button = tk.Button(frame, text="Select File and Decode", command=lambda: run_decode(modules[selected_module.get()][1], decode_output_text))
decode_button.pack(pady=5)

# Dropdown to select algorithm
selected_module = tk.StringVar(value="1-RSA")
module_dropdown = ttk.Combobox(frame, textvariable=selected_module, values=list(modules.keys()), state="readonly")
module_dropdown.pack(pady=5)

root.mainloop()