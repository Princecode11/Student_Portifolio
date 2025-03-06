import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime
import csv
import os

# File to store transactions
FILE_NAME = "transactions.csv"

# Global list to store transactions
transactions = []

# Load transactions from file (if it exists)
def load_transactions():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append({
                    "date": row["date"],
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "type": row["type"]
                })
        refresh_table()

# Save transactions to file
def save_transactions():
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["date", "amount", "category", "type"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for t in transactions:
            writer.writerow(t)
    messagebox.showinfo("Success", "Transactions saved successfully!")

# Function to add a transaction
def add_transaction():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        transaction_type = type_var.get()

        if not category or not transaction_type:
            raise ValueError("Category or Type cannot be empty!")

        transaction = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount,
            "category": category,
            "type": transaction_type
        }
        transactions.append(transaction)
        refresh_table()
        save_transactions()  # Save immediately after adding
        clear_fields()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to refresh the transactions table and totals
def refresh_table():
    for row in transaction_table.get_children():
        transaction_table.delete(row)
    for t in transactions:
        transaction_table.insert("", tk.END, values=(t["date"], t["amount"], t["category"], t["type"]))
    update_totals()

# Function to delete the selected transaction
def delete_transaction():
    selected_item = transaction_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "No transaction selected!")
        return

    confirm = messagebox.askyesno("Delete", "Are you sure you want to delete the selected transaction?")
    if confirm:
        # Get the selected item's values
        item_values = transaction_table.item(selected_item, "values")
        for t in transactions:
            if t["date"] == item_values[0] and str(t["amount"]) == item_values[1] and t["category"] == item_values[2] and t["type"] == item_values[3]:
                transactions.remove(t)
                break
        refresh_table()
        save_transactions()  # Save after deletion
        messagebox.showinfo("Success", "Transaction deleted successfully!")

# Function to update income, expenses, and balance totals
def update_totals():
    total_income = sum(t["amount"] for t in transactions if t["type"] == "Income")
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "Expense")
    final_balance = total_income - total_expenses

    income_label_var.set(f"Total Income: ${total_income:.2f}")
    expenses_label_var.set(f"Total Expenses: ${total_expenses:.2f}")
    balance_label_var.set(f"Final Balance: ${final_balance:.2f}")

# Function to clear input fields
def clear_fields():
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    type_var.set("")

# Function to exit the application
def exit_app():
    save_transactions()  # Save before exiting
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Personal Finance Manager")

# Input Section
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(fill="x")

tk.Label(input_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
amount_entry = tk.Entry(input_frame)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
category_entry = tk.Entry(input_frame)
category_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Type:").grid(row=2, column=0, padx=5, pady=5)
type_var = tk.StringVar(value="")
income_radio = tk.Radiobutton(input_frame, text="Income", variable=type_var, value="Income")
income_radio.grid(row=2, column=1, sticky="w")
expense_radio = tk.Radiobutton(input_frame, text="Expense", variable=type_var, value="Expense")
expense_radio.grid(row=2, column=2, sticky="w")

tk.Button(input_frame, text="Add Transaction", command=add_transaction).grid(row=3, column=0, columnspan=3, pady=10)

# Transactions Table
table_frame = tk.Frame(root, padx=10, pady=10)
table_frame.pack(fill="both", expand=True)

columns = ("Date", "Amount", "Category", "Type")
transaction_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
for col in columns:
    transaction_table.heading(col, text=col)
    transaction_table.column(col, anchor="center", width=100)
transaction_table.pack(fill="both", expand=True)

# Totals Section
totals_frame = tk.Frame(root, padx=10, pady=10)
totals_frame.pack(fill="x")

income_label_var = tk.StringVar(value="Total Income: $0.00")
expenses_label_var = tk.StringVar(value="Total Expenses: $0.00")
balance_label_var = tk.StringVar(value="Final Balance: $0.00")

income_label = tk.Label(totals_frame, textvariable=income_label_var, font=("Arial", 12), fg="green")
income_label.grid(row=0, column=0, padx=5, pady=5)

expenses_label = tk.Label(totals_frame, textvariable=expenses_label_var, font=("Arial", 12), fg="red")
expenses_label.grid(row=0, column=1, padx=5, pady=5)

balance_label = tk.Label(totals_frame, textvariable=balance_label_var, font=("Arial", 12), fg="blue")
balance_label.grid(row=0, column=2, padx=5, pady=5)

# Buttons Section
button_frame = tk.Frame(root, padx=10, pady=10)
button_frame.pack(fill="x")

tk.Button(button_frame, text="Delete Transaction", command=delete_transaction).pack(side="left", padx=5)
tk.Button(button_frame, text="Save Transactions", command=save_transactions).pack(side="left", padx=5)
tk.Button(button_frame, text="Exit", command=exit_app).pack(side="right", padx=5)

# Load transactions at the start 
load_transactions()

# Run the application
root.mainloop()
