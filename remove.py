import tkinter as tk
import pyperclip

def paste_and_process():
    remove_text = remove_entry.get()  # Get the text to be removed from the input
    clipboard_text = pyperclip.paste()  # Get current clipboard

    # Split the input text by commas, remove leading/trailing whitespace, and remove each part
    strings_to_remove = [s.strip() for s in remove_text.split(",")]
    processed_text = clipboard_text
    for string in strings_to_remove:
        processed_text = processed_text.replace(string, "")
    
    input_box.delete("1.0", tk.END)
    input_box.insert(tk.END, clipboard_text)
    
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, processed_text)  # Show processed text in output
    
    pyperclip.copy(processed_text.strip())  # Automatically copy processed text

# GUI
root = tk.Tk()
root.title("GPT String Remover")

# Input for removals
remove_label = tk.Label(root, text="Text to Remove (comma-separated):")
remove_label.pack()
remove_entry = tk.Entry(root, width=50)
remove_entry.pack()

# Input text box
input_label = tk.Label(root, text="Input:")
input_label.pack()
input_box = tk.Text(root, height=10, width=50)
input_box.pack()

# Output text box
output_label = tk.Label(root, text="Output:")
output_label.pack()
output_box = tk.Text(root, height=10, width=50)
output_box.pack()

# Button
process_button = tk.Button(root, text="Paste, Process, and Copy", command=paste_and_process)
process_button.pack(pady=10)

root.mainloop()