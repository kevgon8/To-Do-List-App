import tkinter as tk
import ttkbootstrap as ttk

#set to avoid duplicate tasks(declared on top cuz im too lazy to think where to put it)
existing_tasks = set()
checkbutton_var = {}

def main():
    tasks = process_text_input(tasks_entry)
    create_txtfile(tasks)
    create_checkbox()

#func 2 read all tasks and store in set
def process_text_input(text_widget):
    tasks_set = set()
    k = 1
    while True:
        start_index = f"{k}.0"
        end_index = f"{k}.end"
        line = text_widget.get(start_index, end_index).strip()
        if line:
            tasks_set.add(line)
        else:
            break
        k += 1

    return tasks_set

#func 2 add tasks in txtfile
def create_txtfile(tasks_set):
    with open("tasks.txt", "w") as file:
        for task in tasks_set:
            file.write(f"{task}\n")

#func 2 create check bxs in tab2
def create_checkbox():
    with open("tasks.txt", "r") as file:
        for task in file:
            if task.strip() not in existing_tasks:
                check_var = tk.BooleanVar(value=False)
                checkbutton_var[task.strip()] = check_var
                check_button = ttk.Checkbutton(master=tab2, text=task.strip(), command=cal_progress, variable=check_var, onvalue=True, offvalue=False)
                check_button.pack(anchor="w", side="top", pady=6, padx=(3,0))
                existing_tasks.add(task.strip())

#func to clear all tasks
def clear_tasks():
    for widget in tab2.winfo_children():
        if isinstance(widget, ttk.Checkbutton):
            widget.destroy()
            existing_tasks.clear()
    progress["value"] = 0

#func 2 cal progress
def cal_progress():
    progress_count = 0
    total_tasks = 0
    for task, bool_var in checkbutton_var.items():
        if bool_var.get():
            progress_count += 1
        total_tasks += 1
    ttl = (progress_count/total_tasks)*100
    progress["value"] = ttl


def add_and_cal_progress():
    main()
    cal_progress()


#main window and notebook for tabs
window = ttk.Window(themename="darkly")
window.title("To-Do List")
window.geometry("600x855")
notebook = ttk.Notebook(master=window)

#title
title = ttk.Label(master=window, text="To-Do List", font="calabri 23 bold")
title.pack()

#tabs
tab1 = ttk.Frame(master=notebook, width="513", height="360", relief=tk.SOLID)
tab2 = ttk.Frame(master=notebook, width="513", height="360", relief=tk.SOLID)

notebook.add(tab1, text="Add tasks")
notebook.add(tab2, text="View tasks")
notebook.pack(pady=21)

#tab1
sub_title = ttk.Label(master=tab1, text="Add tasks", font="calibri 17")
sub_title.pack()

tasks_entry = ttk.Text(master=tab1, width="55", height="30")
tasks_entry.pack(pady=(10, 0))

add_button = ttk.Button(master=tab1, text="Add", command=add_and_cal_progress)
add_button.pack(fill="both")

#tab2
clear_tasks = ttk.Button(master=tab2, text="Clear", command=clear_tasks)
clear_tasks.pack(side="bottom", fill="x")
## Progress bar frame
progress_frame = ttk.Frame(master=tab2)
progress_frame.pack(anchor="w", side="bottom", pady=3, padx=(3,0))
## Label and Progress Bar in the frame
progress_label = ttk.Label(master=progress_frame, text="Progress: ", font="Calibri 14 bold")
progress_label.pack(side="left")

progress = ttk.Progressbar(master=progress_frame, maximum=100, length=340)
progress.pack(side="left", padx=(5, 0))


#run
window.mainloop()