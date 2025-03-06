import tkinter as tk
from tkinter import ttk, messagebox

# Data storage
courses = []
teachers = ["Alice", "Bob", "Charlie"]  # Example teacher list
rooms = [{"room": "Room 1", "capacity": 30}, {"room": "Room 2", "capacity": 40}]
timetable = []


# Refresh a table with new data
def refresh_table(table, data, columns):
    for row in table.get_children():
        table.delete(row)
    for item in data:
        table.insert("", tk.END, values=[item[col.lower()] for col in columns])


# Add a new course
def add_course():
    course_name = course_name_entry.get()
    teacher_name = teacher_dropdown.get()
    duration = course_duration_entry.get()

    if not course_name or not teacher_name or not duration.isdigit():
        messagebox.showerror("Error", "Please provide valid course details!")
        return

    # Check for duplicate course names
    if any(course["course"] == course_name for course in courses):
        messagebox.showerror("Error", "Course already exists!")
        return

    courses.append({"course": course_name, "teacher": teacher_name, "duration": int(duration)})
    refresh_table(course_table, courses, ["Course", "Teacher", "Duration"])
    clear_course_fields()


# Add a room
def add_room():
    room_name = room_name_entry.get()
    capacity = room_capacity_entry.get()

    if not room_name or not capacity.isdigit():
        messagebox.showerror("Error", "Please provide valid room details!")
        return

    # Check for duplicate room names
    if any(room["room"] == room_name for room in rooms):
        messagebox.showerror("Error", "Room already exists!")
        return

    rooms.append({"room": room_name, "capacity": int(capacity)})
    refresh_table(room_table, rooms, ["Room", "Capacity"])
    clear_room_fields()


# Clear input fields for courses
def clear_course_fields():
    course_name_entry.delete(0, tk.END)
    course_duration_entry.delete(0, tk.END)
    teacher_dropdown.set(teachers[0])


# Clear input fields for rooms
def clear_room_fields():
    room_name_entry.delete(0, tk.END)
    room_capacity_entry.delete(0, tk.END)


# Edit selected row
def edit_selected_course():
    selected_item = course_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "No course selected for editing!")
        return

    # Get current values
    item = course_table.item(selected_item)["values"]
    course_name_entry.insert(0, item[0])
    teacher_dropdown.set(item[1])
    course_duration_entry.insert(0, item[2])

    # Remove old entry
    courses[:] = [c for c in courses if c["course"] != item[0]]
    refresh_table(course_table, courses, ["Course", "Teacher", "Duration"])


# Delete selected row
def delete_selected_course():
    selected_item = course_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "No course selected for deletion!")
        return

    # Get current values and remove entry
    item = course_table.item(selected_item)["values"]
    courses[:] = [c for c in courses if c["course"] != item[0]]
    refresh_table(course_table, courses, ["Course", "Teacher", "Duration"])


# Create the main window
root = tk.Tk()
root.title("Improved University Timetable Generator")
root.geometry("900x600")

# Add Course Section
course_frame = tk.LabelFrame(root, text="Add/Edit Course", padx=10, pady=10)
course_frame.pack(fill="x", padx=10, pady=5)

tk.Label(course_frame, text="Course Name:").grid(row=0, column=0, padx=5, pady=5)
course_name_entry = tk.Entry(course_frame)
course_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(course_frame, text="Teacher:").grid(row=0, column=2, padx=5, pady=5)
teacher_dropdown = ttk.Combobox(course_frame, values=teachers, state="readonly")
teacher_dropdown.set(teachers[0])  # Default selection
teacher_dropdown.grid(row=0, column=3, padx=5, pady=5)

tk.Label(course_frame, text="Duration (hours):").grid(row=0, column=4, padx=5, pady=5)
course_duration_entry = tk.Entry(course_frame)
course_duration_entry.grid(row=0, column=5, padx=5, pady=5)

tk.Button(course_frame, text="Add Course", command=add_course).grid(row=0, column=6, padx=5, pady=5)
tk.Button(course_frame, text="Edit Selected", command=edit_selected_course).grid(row=0, column=7, padx=5, pady=5)
tk.Button(course_frame, text="Delete Selected", command=delete_selected_course).grid(row=0, column=8, padx=5, pady=5)

# Add Room Section
room_frame = tk.LabelFrame(root, text="Add Room", padx=10, pady=10)
room_frame.pack(fill="x", padx=10, pady=5)

tk.Label(room_frame, text="Room Name:").grid(row=0, column=0, padx=5, pady=5)
room_name_entry = tk.Entry(room_frame)
room_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(room_frame, text="Capacity:").grid(row=0, column=2, padx=5, pady=5)
room_capacity_entry = tk.Entry(room_frame)
room_capacity_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Button(room_frame, text="Add Room", command=add_room).grid(row=0, column=4, padx=5, pady=5)

# Course Table
course_table_frame = tk.LabelFrame(root, text="Courses")
course_table_frame.pack(fill="both", expand=True, padx=10, pady=10)

course_table = ttk.Treeview(course_table_frame, columns=["Course", "Teacher", "Duration"], show="headings")
for col in ["Course", "Teacher", "Duration"]:
    course_table.heading(col, text=col)
    course_table.column(col, width=100)
course_table.pack(fill="both", expand=True)

# Room Table
room_table_frame = tk.LabelFrame(root, text="Rooms")
room_table_frame.pack(fill="both", expand=True, padx=10, pady=10)

room_table = ttk.Treeview(room_table_frame, columns=["Room", "Capacity"], show="headings")
for col in ["Room", "Capacity"]:
    room_table.heading(col, text=col)
    room_table.column(col, width=100)
room_table.pack(fill="both", expand=True)

# Start the main loop
root.mainloop()
