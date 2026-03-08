import customtkinter as ctk
from tkinter import ttk, messagebox
import mysql.connector

# ---------------- Database Connection ----------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="RAHUL123",  # Your MySQL password
    database="course_management"
)
cursor = db.cursor()

# ---------------- Functions ----------------
def load_subjects():
    cursor.execute("SELECT * FROM subjects")
    return cursor.fetchall()

def load_teachers(filter_subject=None):
    sql = """SELECT teachers.teacher_id, teachers.teacher_name, subjects.subject_name
             FROM teachers JOIN subjects ON teachers.subject_id = subjects.subject_id"""
    if filter_subject:
        sql += " WHERE subjects.subject_name LIKE %s"
        cursor.execute(sql, ('%' + filter_subject + '%',))
    else:
        cursor.execute(sql)
    return cursor.fetchall()

def load_students(filter_subject=None):
    sql = """SELECT students.student_id, students.student_name, subjects.subject_name
             FROM students JOIN subjects ON students.subject_id = subjects.subject_id"""
    if filter_subject:
        sql += " WHERE subjects.subject_name LIKE %s"
        cursor.execute(sql, ('%' + filter_subject + '%',))
    else:
        cursor.execute(sql)
    return cursor.fetchall()

# ---------------- CRUD Functions ----------------
def add_subject():
    name = subject_entry.get()
    if name:
        cursor.execute("INSERT INTO subjects (subject_name) VALUES (%s)", (name,))
        db.commit()
        subject_entry.delete(0, ctk.END)
        display_subjects()
        refresh_subject_dropdowns()
        update_dashboard()
    else:
        messagebox.showwarning("Error", "Enter subject name!")

def edit_subject():
    selected = subject_tree.selection()
    if not selected:
        messagebox.showwarning("Error", "Select a subject!")
        return
    subject_id = subject_tree.item(selected[0])['values'][0]
    new_name = subject_entry.get()
    if new_name:
        cursor.execute("UPDATE subjects SET subject_name=%s WHERE subject_id=%s", (new_name, subject_id))
        db.commit()
        display_subjects()
        refresh_subject_dropdowns()
        update_dashboard()

def delete_subject():
    selected = subject_tree.selection()
    if not selected:
        messagebox.showwarning("Error", "Select a subject!")
        return
    subject_id = subject_tree.item(selected[0])['values'][0]
    cursor.execute("DELETE FROM subjects WHERE subject_id=%s", (subject_id,))
    db.commit()
    display_subjects()
    refresh_subject_dropdowns()
    update_dashboard()

def add_teacher():
    name = teacher_entry.get()
    subject = teacher_subject_var.get()
    if name and subject:
        subject_id = int(subject.split(" - ")[0])
        cursor.execute("INSERT INTO teachers (teacher_name, subject_id) VALUES (%s,%s)", (name, subject_id))
        db.commit()
        teacher_entry.delete(0, ctk.END)
        display_teachers()
        update_dashboard()
    else:
        messagebox.showwarning("Error", "Enter name and select subject!")

def edit_teacher():
    selected = teacher_tree.selection()
    if not selected:
        messagebox.showwarning("Error", "Select a teacher!")
        return
    teacher_id = teacher_tree.item(selected[0])['values'][0]
    name = teacher_entry.get()
    subject = teacher_subject_var.get()
    if name and subject:
        subject_id = int(subject.split(" - ")[0])
        cursor.execute("UPDATE teachers SET teacher_name=%s, subject_id=%s WHERE teacher_id=%s", (name, subject_id, teacher_id))
        db.commit()
        display_teachers()
        update_dashboard()

def delete_teacher():
    selected = teacher_tree.selection()
    if not selected:
        messagebox.showwarning("Error", "Select a teacher!")
        return
    teacher_id = teacher_tree.item(selected[0])['values'][0]
    cursor.execute("DELETE FROM teachers WHERE teacher_id=%s", (teacher_id,))
    db.commit()
    display_teachers()
    update_dashboard()

def add_student():
    name = student_entry.get()
    subject = student_subject_var.get()
    if name and subject:
        subject_id = int(subject.split(" - ")[0])
        cursor.execute("INSERT INTO students (student_name, subject_id) VALUES (%s,%s)", (name, subject_id))
        db.commit()
        student_entry.delete(0, ctk.END)
        display_students()
        update_dashboard()
    else:
        messagebox.showwarning("Error", "Enter name and select subject!")

def edit_student():
    selected = student_tree.selection()
    if not selected:
        messagebox.showwarning("Error", "Select a student!")
        return
    student_id = student_tree.item(selected[0])['values'][0]
    name = student_entry.get()
    subject = student_subject_var.get()
    if name and subject:
        subject_id = int(subject.split(" - ")[0])
        cursor.execute("UPDATE students SET student_name=%s, subject_id=%s WHERE student_id=%s", (name, subject_id, student_id))
        db.commit()
        display_students()
        update_dashboard()

def delete_student():
    selected = student_tree.selection()
    if not selected:
        messagebox.showwarning("Error", "Select a student!")
        return
    student_id = student_tree.item(selected[0])['values'][0]
    cursor.execute("DELETE FROM students WHERE student_id=%s", (student_id,))
    db.commit()
    display_students()
    update_dashboard()

# ---------------- Display Functions ----------------
def display_subjects():
    subject_tree.delete(*subject_tree.get_children())
    for subj in load_subjects():
        subject_tree.insert("", "end", values=subj)

def display_teachers():
    teacher_tree.delete(*teacher_tree.get_children())
    filter_subject = teacher_filter_entry.get()
    for t in load_teachers(filter_subject):
        teacher_tree.insert("", "end", values=t)

def display_students():
    student_tree.delete(*student_tree.get_children())
    filter_subject = student_filter_entry.get()
    for s in load_students(filter_subject):
        student_tree.insert("", "end", values=s)

def refresh_subject_dropdowns():
    cursor.execute("SELECT subject_id, subject_name FROM subjects")
    subjects = cursor.fetchall()
    teacher_subject_dropdown.configure(values=[f"{s[0]} - {s[1]}" for s in subjects])
    student_subject_dropdown.configure(values=[f"{s[0]} - {s[1]}" for s in subjects])

# ---------------- Dashboard ----------------
def update_dashboard():
    cursor.execute("SELECT COUNT(*) FROM subjects")
    subjects_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM teachers")
    teachers_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM students")
    students_count = cursor.fetchone()[0]

    dashboard_subjects_label.configure(text=f"Subjects: {subjects_count}")
    dashboard_teachers_label.configure(text=f"Teachers: {teachers_count}")
    dashboard_students_label.configure(text=f"Students: {students_count}")

# ---------------- GUI Setup ----------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Course Management System")
root.geometry("1200x750")

# ---------------- Dashboard ----------------
dashboard_frame = ctk.CTkFrame(root)
dashboard_frame.pack(fill="x", padx=20, pady=10)

dashboard_subjects_label = ctk.CTkLabel(dashboard_frame, text="Subjects: 0", font=ctk.CTkFont(size=16, weight="bold"))
dashboard_subjects_label.pack(side="left", padx=30)
dashboard_teachers_label = ctk.CTkLabel(dashboard_frame, text="Teachers: 0", font=ctk.CTkFont(size=16, weight="bold"))
dashboard_teachers_label.pack(side="left", padx=30)
dashboard_students_label = ctk.CTkLabel(dashboard_frame, text="Students: 0", font=ctk.CTkFont(size=16, weight="bold"))
dashboard_students_label.pack(side="left", padx=30)

# ---------------- Tabview ----------------
tabview = ctk.CTkTabview(root)
tabview.pack(fill="both", expand=True, padx=20, pady=10)

# -------- Subjects Tab --------
tabview.add("Subjects")
subject_frame = ctk.CTkFrame(tabview.tab("Subjects"))
subject_frame.pack(fill="both", expand=True, padx=10, pady=10)

subject_tree = ttk.Treeview(subject_frame, columns=("ID", "Name"), show='headings')
subject_tree.heading("ID", text="ID")
subject_tree.heading("Name", text="Subject Name")
subject_tree.pack(fill="both", expand=True, pady=10)

subject_entry = ctk.CTkEntry(subject_frame, placeholder_text="Subject Name")
subject_entry.pack(pady=5)

ctk.CTkButton(subject_frame, text="Add", command=add_subject).pack(pady=5)
ctk.CTkButton(subject_frame, text="Edit", command=edit_subject).pack(pady=5)
ctk.CTkButton(subject_frame, text="Delete", command=delete_subject).pack(pady=5)

# -------- Teachers Tab --------
tabview.add("Teachers")
teacher_frame = ctk.CTkFrame(tabview.tab("Teachers"))
teacher_frame.pack(fill="both", expand=True, padx=10, pady=10)

teacher_filter_entry = ctk.CTkEntry(teacher_frame, placeholder_text="Search by subject")
teacher_filter_entry.pack(pady=5)
ctk.CTkButton(teacher_frame, text="Search", command=display_teachers).pack(pady=5)

teacher_tree = ttk.Treeview(teacher_frame, columns=("ID","Name","Subject"), show='headings')
teacher_tree.heading("ID", text="ID")
teacher_tree.heading("Name", text="Teacher Name")
teacher_tree.heading("Subject", text="Subject")
teacher_tree.pack(fill="both", expand=True, pady=10)

teacher_entry = ctk.CTkEntry(teacher_frame, placeholder_text="Teacher Name")
teacher_entry.pack(pady=5)
teacher_subject_var = ctk.StringVar()
teacher_subject_dropdown = ctk.CTkComboBox(teacher_frame, variable=teacher_subject_var)
teacher_subject_dropdown.pack(pady=5)

ctk.CTkButton(teacher_frame, text="Add", command=add_teacher).pack(pady=5)
ctk.CTkButton(teacher_frame, text="Edit", command=edit_teacher).pack(pady=5)
ctk.CTkButton(teacher_frame, text="Delete", command=delete_teacher).pack(pady=5)

# -------- Students Tab --------
tabview.add("Students")
student_frame = ctk.CTkFrame(tabview.tab("Students"))
student_frame.pack(fill="both", expand=True, padx=10, pady=10)

student_filter_entry = ctk.CTkEntry(student_frame, placeholder_text="Search by subject")
student_filter_entry.pack(pady=5)
ctk.CTkButton(student_frame, text="Search", command=display_students).pack(pady=5)

student_tree = ttk.Treeview(student_frame, columns=("ID","Name","Subject"), show='headings')
student_tree.heading("ID", text="ID")
student_tree.heading("Name", text="Student Name")
student_tree.heading("Subject", text="Subject")
student_tree.pack(fill="both", expand=True, pady=10)

student_entry = ctk.CTkEntry(student_frame, placeholder_text="Student Name")
student_entry.pack(pady=5)
student_subject_var = ctk.StringVar()
student_subject_dropdown = ctk.CTkComboBox(student_frame, variable=student_subject_var)
student_subject_dropdown.pack(pady=5)

ctk.CTkButton(student_frame, text="Add", command=add_student).pack(pady=5)
ctk.CTkButton(student_frame, text="Edit", command=edit_student).pack(pady=5)
ctk.CTkButton(student_frame, text="Delete", command=delete_student).pack(pady=5)

# ---------------- Initial Load ----------------
refresh_subject_dropdowns()
display_subjects()
display_teachers()
display_students()
update_dashboard()

root.mainloop()
