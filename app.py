import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import importlib
import os

tabs = {
    "1E": "solution_1_encode",
    "1D": "solution_1_decode",
    "2E": "solution_2_encode",
    "2D": "solution_2_decode",
    "3E-Quot": "solution_3_encode",
    "3D-Quot": "solution_3_decode",
    "4E-lettercase": "solution_4_encode",
    "4D-lettercase": "solution_4_decode",
    "5E-space": "solution_5_encode",
    "5D-space": "solution_5_decode"
}

def open_html_file():
    file_path = filedialog.askopenfilename(
        title="Choose HTML file",
        filetypes=[("HTML files", "*.html")]
    )
    return file_path

def run_algorithm(module_name, is_encode, message_entry=None):
    html_path = open_html_file()
    if not html_path:
        return

    try:
        with open(html_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Imports algorithms module
        module = importlib.import_module(module_name)
        
        if is_encode: 
            message = message_entry.get().strip() if message_entry else ""
            if not message: 
                messagebox.showerror("ERROR", "Enter your message!")
                return
            
            # It calls the HTML processing function with the message
            modified_html = module.process_html(html_content, message)
            
            output_file_path = os.path.join(os.path.dirname(html_path), "output.html")
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(modified_html)
            
            messagebox.showinfo("Success", f"File {output_file_path} has been safe.")
        
        else: #TODO
            password = module.extract_password(html_content)
            output_label.config(text=f"Hasło: {password}")
    
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się przetworzyć pliku: {e}")

# main
root = tk.Tk()
root.title("Aplikacja z zakładkami")
root.geometry("500x400")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# based on `tabs`
for tab_name, module_name in tabs.items():
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_name)
    
    is_encode = "E" in tab_name
    
    message_entry = None  # None for decoding tabs
    
    if is_encode:
        tk.Label(tab, text="Message:").pack(pady=5)
        message_entry = tk.Entry(tab, width=40) 
        message_entry.pack(pady=5)
    
    run_button = tk.Button(tab, text="Run the algorithm", command=lambda m=module_name, e=is_encode, me=message_entry: run_algorithm(m, e, me))
    run_button.pack(pady=10)

output_label = tk.Label(root, text="The result will appear here", wraplength=450)
output_label.pack(pady=10)

root.mainloop()
