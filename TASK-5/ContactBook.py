import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Dictionary to store contacts
contacts = {}

# Function to load contacts from the JSON file
def load_contacts():
    global contacts
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            contacts = json.load(file)
    else:
        contacts = {}

# Function to save contacts to the JSON file
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Function to add a contact
def add_contact(name, phone, email, address):
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    save_contacts()
    update_total_label()

# Function to update a contact
def update_contact(name, phone=None, email=None, address=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        save_contacts()

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        save_contacts()
        update_total_label()

# Function to refresh the contact list in the treeview
def refresh_contact_list(tree):
    for row in tree.get_children():
        tree.delete(row)
    for name, details in contacts.items():
        tree.insert("", "end", values=(name, details['phone'], details['email'], details['address']))

# Function to search for a contact
def search_contact(query, tree):
    for row in tree.get_children():
        tree.delete(row)
    results = {name: details for name, details in contacts.items() if query.lower() in name.lower() or query in details['phone']}
    for name, details in results.items():
        tree.insert("", "end", values=(name, details['phone'], details['email'], details['address']))

# Function to handle adding a new contact
def handle_add_contact():
    add_window = tk.Toplevel(root)
    add_window.title("Add Contact")

    add_frame = tk.Frame(add_window, bg="#e0f7fa", pady=20, padx=20)
    add_frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(add_frame, text="Add New Contact", font=("Helvetica", 16, "bold"), bg="#e0f7fa").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(add_frame, text="Name:", font=("Helvetica", 12), bg="#e0f7fa").grid(row=1, column=0, sticky=tk.E, padx=10, pady=5)
    entry_name = tk.Entry(add_frame, font=("Helvetica", 12))
    entry_name.grid(row=1, column=1, pady=5)

    tk.Label(add_frame, text="Phone:", font=("Helvetica", 12), bg="#e0f7fa").grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)
    entry_phone = tk.Entry(add_frame, font=("Helvetica", 12))
    entry_phone.grid(row=2, column=1, pady=5)

    tk.Label(add_frame, text="Email:", font=("Helvetica", 12), bg="#e0f7fa").grid(row=3, column=0, sticky=tk.E, padx=10, pady=5)
    entry_email = tk.Entry(add_frame, font=("Helvetica", 12))
    entry_email.grid(row=3, column=1, pady=5)

    tk.Label(add_frame, text="Address:", font=("Helvetica", 12), bg="#e0f7fa").grid(row=4, column=0, sticky=tk.E, padx=10, pady=5)
    entry_address = tk.Entry(add_frame, font=("Helvetica", 12))
    entry_address.grid(row=4, column=1, pady=5)

    def save_contact():
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()
        add_contact(name, phone, email, address)
        refresh_contact_list(tree_view)
        add_window.destroy()

    tk.Button(add_frame, text="Add Contact", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=save_contact).grid(row=5, column=0, columnspan=2, pady=10)

# Function to handle editing a contact
def handle_edit_contact():
    selected_item = tree_view.selection()
    if selected_item:
        item = tree_view.item(selected_item)
        name = item['values'][0]

        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Contact")

        edit_frame = tk.Frame(edit_window, bg="#e0f7fa", pady=20, padx=20)
        edit_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(edit_frame, text="Edit Contact", font=("Helvetica", 16, "bold"), bg="#e0f7fa").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(edit_frame, text="Name:", font=("Helvetica", 12), bg="#e0f7fa").grid(row=1, column=0, sticky=tk.E, padx=10, pady=5)
        entry_name = tk.Entry(edit_frame, font=("Helvetica", 12))
        entry_name.insert(0, name)
        entry_name.grid(row=1, column=1, pady=5)

        tk.Label(edit_frame, text="Phone:", font=("Helvetica", 12), bg="#e0f7fa").grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)
        entry_phone = tk.Entry(edit_frame, font=("Helvetica", 12))
        entry_phone.insert(0, contacts[name]['phone'])
        entry_phone.grid(row=2, column=1, pady=5)

        tk.Label(edit_frame, text="Email:", font=("Helvetica", 12), bg="#e0f7fa").grid(row=3, column=0, sticky=tk.E, padx=10, pady=5)
        entry_email = tk.Entry(edit_frame, font=("Helvetica", 12))
        entry_email.insert(0, contacts[name]['email'])
        entry_email.grid(row=3, column=1, pady=5)

        tk.Label(edit_frame, text="Address:", font=("Helvetica", 12), bg="#e0f7fa").grid(row=4, column=0, sticky=tk.E, padx=10, pady=5)
        entry_address = tk.Entry(edit_frame, font=("Helvetica", 12))
        entry_address.insert(0, contacts[name]['address'])
        entry_address.grid(row=4, column=1, pady=5)

        def save_edit():
            new_name = entry_name.get()
            phone = entry_phone.get()
            email = entry_email.get()
            address = entry_address.get()
            if new_name != name:
                contacts[new_name] = contacts.pop(name)
            update_contact(new_name, phone, email, address)
            refresh_contact_list(tree_view)
            edit_window.destroy()

        tk.Button(edit_frame, text="Save Changes", font=("Helvetica", 12), bg="#2196F3", fg="white", command=save_edit).grid(row=5, column=0, columnspan=2, pady=10)

# Function to handle deleting a contact
def handle_delete_contact():
    selected_item = tree_view.selection()
    if selected_item:
        item = tree_view.item(selected_item)
        name = item['values'][0]
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {name}?")
        if confirm:
            delete_contact(name)
            refresh_contact_list(tree_view)
            update_button.pack_forget()
            delete_button.pack_forget()

# Function to handle contact selection
def on_contact_select(event):
    selected_item = tree_view.selection()
    if selected_item:
        update_button.pack(side=tk.LEFT, padx=10)
        delete_button.pack(side=tk.LEFT, padx=10)
    else:
        update_button.pack_forget()
        delete_button.pack_forget()

# Function to update total contacts label
def update_total_label():
    total_label.config(text=f"Total Contacts: {len(contacts)}")

# Main application window
root = tk.Tk()
root.title("Contact Management System")
root.state('zoomed')

# Configure style for Treeview
style = ttk.Style()
style.configure("Treeview.Heading", font=("Helvetica", 12))
style.configure("Treeview", font=("Helvetica", 11))

# Top frame for search and add contact
top_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
top_frame.pack(side=tk.TOP, fill=tk.X)

# Search box
tk.Label(top_frame, text="Name Search:", font=("Helvetica", 12), bg="#f0f0f0").pack(side=tk.LEFT, padx=10)
entry_search = tk.Entry(top_frame, font=("Helvetica", 12))
entry_search.pack(side=tk.LEFT)
tk.Button(top_frame, text="Search", font=("Helvetica", 12), bg="#2196F3", fg="white", command=lambda: search_contact(entry_search.get(), tree_view)).pack(side=tk.LEFT, padx=10)

# Total Contacts frame
total_frame = tk.Frame(top_frame, bg="#f0f0f0")
total_frame.pack(side=tk.RIGHT, padx=10)
total_label = tk.Label(total_frame, text=f"Total Contacts: {len(contacts)}", font=("Helvetica", 12), bg="#f0f0f0")
total_label.pack()

# Add Contact button
tk.Button(top_frame, text="Add Contact", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=handle_add_contact).pack(side=tk.RIGHT, padx=10)

# Frame for contact list
list_frame = tk.Frame(root)
list_frame.pack(fill=tk.BOTH, expand=True)

# Treeview for displaying contacts
tree_view = ttk.Treeview(list_frame, columns=("Name", "Phone", "Email", "Address"), show='headings')
tree_view.heading("Name", text="Name")
tree_view.heading("Phone", text="Phone")
tree_view.heading("Email", text="Email")
tree_view.heading("Address", text="Address")
tree_view.pack(fill=tk.BOTH, expand=True)

# Center align the columns
for col in tree_view['columns']:
    tree_view.column(col, anchor=tk.CENTER)
    tree_view.heading(col, anchor=tk.CENTER)

# Edit and Delete buttons (initially hidden)
update_button = tk.Button(root, text="Edit Contact", font=("Helvetica", 12), bg="#FFC107", fg="white", command=handle_edit_contact)
delete_button = tk.Button(root, text="Delete Contact", font=("Helvetica", 12), bg="#F44336", fg="white", command=handle_delete_contact)

# Bind the contact selection event
tree_view.bind("<<TreeviewSelect>>", on_contact_select)

# Load contacts from file
load_contacts()

# Initial load of contact list and update total contacts label
refresh_contact_list(tree_view)
update_total_label()

root.mainloop()
