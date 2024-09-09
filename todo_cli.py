import tkinter as tk
from tkinter import ttk

def convert():
	print(output_str.set("You clicked!!!"))

# Create a window
window = tk.Tk()
window.title("Demo")
window.geometry("400x200")

# Title text/widget
title_label = ttk.Label(master=window, text="Miles to Kilometers", font="Calibri 24 bold")
title_label.pack()

# Input field
input_frame = tk.Frame(master=window)
entry_int = tk.IntVar()
usr_entry = tk.Entry(master=input_frame, textvariable=entry_int)
button = tk.Button(master=input_frame, text="Convert", command=convert)
usr_entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady=10)

# Output text/widget
output_str = tk.StringVar()
output = ttk.Label(master=window, text="Output", font="Calibri 20", textvariable=output_str)
output.pack()

# Run
window.mainloop()
