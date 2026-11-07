import tkinter as tk
from tkinter import messagebox
import json
import os

# The local file where your data will be stored
DATA_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the local JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return [] # Return empty list if file is corrupted
    return []

def save_tasks(tasks):
    """Saves tasks to the local JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file)

def save_current_state():
    """Grabs all tasks from the UI and saves them."""
    tasks = task_listbox.get(0, tk.END)
    save_tasks(tasks)

def add_task():
    """Adds a new task to the list and saves."""
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_current_state()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    """Deletes the selected task and saves."""
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_current_state()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# --- UI Setup ---
root = tk.Tk()
root.title("Simple To-Do List")
root.geometry("350x450")
root.config(padx=20, pady=20)

# Entry Box for new tasks
task_entry = tk.Entry(root, width=35, font=("Arial", 12))
task_entry.pack(pady=(0, 10))

# Add Button
add_button = tk.Button(root, text="Add Task", width=15, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=add_task)
add_button.pack(pady=(0, 15))

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 11), selectbackground="#a6a6a6")
task_listbox.pack(pady=(0, 15))

# Delete Button
delete_button = tk.Button(root, text="Delete Selected", width=15, bg="#f44336", fg="white", font=("Arial", 10, "bold"), command=delete_task)
delete_button.pack()

# Load existing tasks when the app starts
for t in load_tasks():
    task_listbox.insert(tk.END, t)

# Run the app
root.mainloop()