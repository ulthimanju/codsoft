import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = json.load(file)
            for task in tasks:
                if "date" not in task:
                    task["date"] = ""
            return tasks
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file)

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("600x500")
        self.tasks = load_tasks()

        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
        style.configure("Treeview", font=("Helvetica", 10), rowheight=25)
        style.configure("TButton", font=("Helvetica", 10, "bold"), background="#4CAF50", foreground="white")
        style.map("TButton", background=[('active', '#45a049')])

        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(self.main_frame, columns=("Task", "Status", "Date"), show='headings', selectmode="browse")
        self.tree.heading("Task", text="Task")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Date", text="Date")
        self.tree.column("Task", anchor=tk.W, width=200)
        self.tree.column("Status", anchor=tk.CENTER, width=80)
        self.tree.column("Date", anchor=tk.CENTER, width=100)
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.entry_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.entry_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

        tk.Label(self.entry_frame, text="Task:", bg="#f0f0f0", font=("Helvetica", 10, "bold")).grid(row=0, column=0, padx=5, sticky="e")
        self.entry = tk.Entry(self.entry_frame, font=("Helvetica", 10))
        self.entry.grid(row=0, column=1, padx=5, sticky="ew")

        tk.Label(self.entry_frame, text="Date:", bg="#f0f0f0", font=("Helvetica", 10, "bold")).grid(row=0, column=2, padx=5, sticky="e")
        self.date_picker = DateEntry(self.entry_frame, width=12, background='darkblue', foreground='white', borderwidth=2, font=("Helvetica", 10))
        self.date_picker.grid(row=0, column=3, padx=5, sticky="ew")

        self.entry_frame.columnconfigure(1, weight=1)
        self.entry_frame.columnconfigure(3, weight=1)

        self.button_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.add_button = ttk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.modify_button = ttk.Button(self.button_frame, text="Modify Task", command=self.modify_task, state=tk.DISABLED)
        self.modify_button.grid(row=0, column=1, padx=5)

        self.complete_button = ttk.Button(self.button_frame, text="Change Status", command=self.complete_task, state=tk.DISABLED)
        self.complete_button.grid(row=0, column=2, padx=5)

        self.delete_button = ttk.Button(self.button_frame, text="Delete Task", command=self.delete_task, state=tk.DISABLED)
        self.delete_button.grid(row=0, column=3, padx=5)

        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        self.update_tree()
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)

    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            self.modify_button.state(["!disabled"])
            self.complete_button.state(["!disabled"])
            self.delete_button.state(["!disabled"])
            index = int(selected_item[0]) - 1
            task = self.tasks[index]
            self.entry.delete(0, tk.END)
            self.entry.insert(0, task["task"])
            self.date_picker.set_date(task["date"])
        else:
            self.modify_button.state(["disabled"])
            self.complete_button.state(["disabled"])
            self.delete_button.state(["disabled"])

    def add_task(self):
        task = self.entry.get()
        date = self.date_picker.get_date()
        if task and date:
            self.tasks.append({"task": task, "completed": False, "date": date.strftime("%Y-%m-%d")})
            self.save_tasks()
            self.update_tree()
            self.entry.delete(0, tk.END)
            self.date_picker.set_date("")
        else:
            messagebox.showwarning("Warning", "You must enter a task and select a date.")

    def modify_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = int(selected_item[0]) - 1
            task = self.tasks[index]
            new_task = self.entry.get()
            new_date = self.date_picker.get_date()
            if new_task and new_date:
                task["task"] = new_task
                task["date"] = new_date.strftime("%Y-%m-%d")
                self.save_tasks()
                self.update_tree()
                self.entry.delete(0, tk.END)
                self.date_picker.set_date("")
            else:
                messagebox.showwarning("Warning", "You must enter a task and select a date.")
        else:
            messagebox.showwarning("Warning", "You must select a task to modify.")

    def complete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = int(selected_item[0]) - 1
            task = self.tasks[index]
            task["completed"] = not task["completed"]
            self.save_tasks()
            self.update_tree()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = int(selected_item[0]) - 1
            del self.tasks[index]
            self.save_tasks()
            self.update_tree()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Not Done"
            self.tree.insert("", "end", iid=i+1, values=(task["task"], status, task["date"]))
        self.modify_button.state(["disabled"])
        self.complete_button.state(["disabled"])
        self.delete_button.state(["disabled"])

    def save_tasks(self):
        save_tasks(self.tasks)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()