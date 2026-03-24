"""
GUI MODULE

Requirement satisfied:
✔ Functional GUI using Tkinter
✔ Modular programming
✔ Error handling with messages
✔ Task deletion feature (improved usability)
"""

import tkinter as tk
from tkinter import messagebox
from scheduler import add_task, execute_task, get_tasks, get_completed_tasks, delete_task
from validation import validate_task
import styles

def start_app():

    # ➤ Add Task
    def add():
        task = task_entry.get()
        priority = priority_entry.get()

        valid, message = validate_task(task, priority)
        if not valid:
            messagebox.showerror("Input Error", message)
            return

        add_task(task, int(priority))
        update_lists()
        task_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)

    # ➤ Execute Highest Priority Task
    def execute():
        task = execute_task()
        if task:
            messagebox.showinfo("Task Executed", f"Completed: {task[1]}")
            update_lists()
        else:
            messagebox.showinfo("Info", "No tasks available")

    # ➤ Delete Selected Task
    def delete_selected():
        selected = task_list.curselection()

        if not selected:
            messagebox.showerror("Error", "Select a task to delete")
            return

        item = task_list.get(selected)

        # Extract task name & priority
        task_name = item.split("   (Priority ")[0]
        priority = int(item.split("Priority ")[1].replace(")", ""))

        success = delete_task(task_name, priority)

        if success:
            messagebox.showinfo("Deleted", "Task removed successfully")
            update_lists()
        else:
            messagebox.showerror("Error", "Could not delete task")

    # ➤ Refresh Lists
    def update_lists():
        task_list.delete(0, tk.END)
        for p, t in get_tasks():
            task_list.insert(tk.END, f"{t}   (Priority {p})")

        completed_list.delete(0, tk.END)
        for t in get_completed_tasks():
            completed_list.insert(tk.END, t)

    # MAIN WINDOW
    root = tk.Tk()
    root.title("Priority Task Scheduler")
    root.geometry("500x520")
    root.config(bg=styles.BG_COLOR)

    # Title
    tk.Label(root, text="Priority Task Scheduler",
             bg=styles.BG_COLOR,
             font=styles.FONT_TITLE).pack(pady=10)

    frame = tk.Frame(root, bg=styles.BG_COLOR)
    frame.pack()

    # Task input
    tk.Label(frame, text="Task:", bg=styles.BG_COLOR,
             font=styles.FONT_MAIN).grid(row=0, column=0, pady=5)

    task_entry = tk.Entry(frame, width=25)
    task_entry.grid(row=0, column=1, pady=5)

    # Priority input
    tk.Label(frame, text="Priority:", bg=styles.BG_COLOR,
             font=styles.FONT_MAIN).grid(row=1, column=0)

    priority_entry = tk.Entry(frame, width=25)
    priority_entry.grid(row=1, column=1)

    # Buttons
    tk.Button(root, text="Add Task",
              bg=styles.BUTTON_COLOR,
              fg=styles.BUTTON_TEXT,
              width=18,
              command=add).pack(pady=5)

    tk.Button(root, text="Execute Highest Priority",
              bg=styles.BUTTON_COLOR,
              fg=styles.BUTTON_TEXT,
              width=22,
              command=execute).pack(pady=5)

    tk.Button(root, text="Delete Selected Task",
              bg="#c0392b",
              fg="white",
              width=22,
              command=delete_selected).pack(pady=5)

    # Scheduled Tasks
    tk.Label(root, text="Scheduled Tasks",
             bg=styles.BG_COLOR,
             font=styles.FONT_MAIN).pack()

    task_list = tk.Listbox(root, width=45, height=8)
    task_list.pack(pady=5)

    # Completed Tasks
    tk.Label(root, text="Completed Tasks",
             bg=styles.BG_COLOR,
             font=styles.FONT_MAIN).pack()

    completed_list = tk.Listbox(root, width=45, height=8)
    completed_list.pack(pady=5)

    root.mainloop()