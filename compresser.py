import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox

def compress_files():
    """Allows user to select multiple files and compress them into a zip file."""
    files = filedialog.askopenfilenames(title="Select Files to Compress")
    
    if not files:
        messagebox.showwarning("No Files Selected", "Please select at least one file.")
        return

    zip_path = filedialog.asksaveasfilename(
        defaultextension=".zip",
        filetypes=[("ZIP files", "*.zip")],
        title="Save ZIP File As"
    )

    if not zip_path:
        messagebox.showwarning("No Destination Selected", "Please select a valid zip file name.")
        return

    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in files:
                zipf.write(file_path, os.path.basename(file_path))

        messagebox.showinfo("Success", f"Files compressed successfully!\nSaved as: {zip_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def compress_folder():
    """Allows user to select a folder and compress its contents into a zip file."""
    folder_path = filedialog.askdirectory(title="Select Folder to Compress")

    if not folder_path:
        messagebox.showwarning("No Folder Selected", "Please select a valid folder.")
        return

    zip_path = filedialog.asksaveasfilename(
        defaultextension=".zip",
        filetypes=[("ZIP files", "*.zip")],
        title="Save ZIP File As"
    )

    if not zip_path:
        messagebox.showwarning("No Destination Selected", "Please select a valid zip file name.")
        return

    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))

        messagebox.showinfo("Success", f"Folder compressed successfully!\nSaved as: {zip_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create GUI
root = tk.Tk()
root.title("File & Folder Compressor")
root.geometry("350x200")
root.resizable(False, False)

# Create buttons
tk.Label(root, text="Select an option:", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Compress Files", command=compress_files, width=20).pack(pady=5)
tk.Button(root, text="Compress Folder", command=compress_folder, width=20).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=5)

# Run GUI
root.mainloop()
