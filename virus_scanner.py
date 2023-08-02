import tkinter as tk
from tkinter import filedialog
import hashlib
import time

def scan_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        loading_screen()
        window.after(3000, lambda: process_file(file_path))

def loading_screen():
    loading_label = tk.Label(window, text="Scanning file...", font=("Arial", 18), fg="green")
    loading_label.pack()
    progress_bar = tk.Label(window, text="|" + " " * 20 + "|", font=("Arial", 18))
    progress_bar.pack()

    for i in range(1, 21):
        progress_bar.config(text="|" + "#" * i + " " * (20 - i) + "|")
        window.update()
        time.sleep(0.15)

    loading_label.pack_forget()
    progress_bar.pack_forget()

def process_file(file_path):
    with open(file_path, 'rb') as file:
        contents = file.read()
        md5_hash = hashlib.md5(contents).hexdigest()
        if md5_hash.lower() in malicious_files:
            result_label.config(text="File is malicious!", fg="red")
        else:
            result_label.config(text="File is safe.", fg="green")
        ask_scan_again()

def ask_scan_again():
    answer = tk.messagebox.askquestion("Scan Again", "Do you want to scan another file?")
    if answer == 'yes':
        result_label.config(text="")
    else:
        result_label.config(text="Thank you!", fg="blue")
        scan_button.config(state=tk.DISABLED)  # Disable the scan button after completion

# Define the malicious file hashes
malicious_files = [
    "3d8fdcf47b3f5d6bdaac4bcf6d8e0552",
    "c6e0c8d782a33ad97e5e3838748a51f9",
    "f814893777bcc2295fff05f00e508da6",
    "adf4210e6c5efd5f9856e16c6a8e8eba"
]

# Create the main window
window = tk.Tk()
window.title("Antivirus Scanner")
window.geometry("500x300")  # Set the window size

# Create welcome label
welcome_label = tk.Label(window, text="Welcome to Virus Scanner", font=("Arial", 24, "bold"))
welcome_label.pack(pady=30)

# Create file selection button
scan_button = tk.Button(window, text="Select File", command=scan_file, width=20)
scan_button.pack()

# Create label to display the scan result
result_label = tk.Label(window, text="", font=("Arial", 18))
result_label.pack()

# Center the window on the screen
window.eval('tk::PlaceWindow . center')

# Run the GUI
window.mainloop()
