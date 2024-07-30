import tkinter as tk
from tkinter import ttk, messagebox

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600")
        self.students = []

        # Create tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.frame1 = tk.Frame(self.notebook)
        self.frame2 = tk.Frame(self.notebook)
        self.frame3 = tk.Frame(self.notebook)
        self.frame4 = tk.Frame(self.notebook)

        self.notebook.add(self.frame1, text="Add Student")
        self.notebook.add(self.frame2, text="View Students")
        self.notebook.add(self.frame3, text="Delete Student")
        self.notebook.add(self.frame4, text="Generate Result")

        # Add student tab
        self.name_label = tk.Label(self.frame1, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.frame1)
        self.name_entry.pack()

        self.roll_no_label = tk.Label(self.frame1, text="Roll No:")
        self.roll_no_label.pack()
        self.roll_no_entry = tk.Entry(self.frame1)
        self.roll_no_entry.pack()

        self.marks_label = tk.Label(self.frame1, text="Marks:")
        self.marks_label.pack()
        self.marks_entry = tk.Entry(self.frame1)
        self.marks_entry.pack()

        self.add_button = tk.Button(self.frame1, text="Add Student", command=self.add_student)
        self.add_button.pack()

        # View students tab
        self.view_text = tk.Text(self.frame2)
        self.view_text.pack()
        self.view_button = tk.Button(self.frame2, text="View Students", command=self.view_students)
        self.view_button.pack()

        # Delete student tab
        self.delete_label = tk.Label(self.frame3, text="Roll No:")
        self.delete_label.pack()
        self.delete_entry = tk.Entry(self.frame3)
        self.delete_entry.pack()
        self.delete_button = tk.Button(self.frame3, text="Delete Student", command=self.delete_student)
        self.delete_button.pack()

        # Generate result tab
        self.result_text = tk.Text(self.frame4)
        self.result_text.pack()
        self.result_button = tk.Button(self.frame4, text="Generate Result", command=self.generate_result)
        self.result_button.pack()

    def add_student(self):
        name = self.name_entry.get()
        roll_no = self.roll_no_entry.get()
        marks = self.marks_entry.get()
        student = Student(name, roll_no, marks)
        self.students.append(student)
        messagebox.showinfo("Success", "Student added successfully")

    def view_students(self):
        self.view_text.delete(1.0, tk.END)
        for student in self.students:
            self.view_text.insert(tk.END, f"Name: {student.name}\nRoll No: {student.roll_no}\nMarks: {student.marks}\n\n")

    def delete_student(self):
        roll_no = self.delete_entry.get()
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                messagebox.showinfo("Success", "Student deleted successfully")
                return
        messagebox.showerror("Error", "Student not found")

    def generate_result(self):
        self.result_text.delete(1.0, tk.END)
        for student in self.students:
            if int(student.marks) >= 40:
                result = "Pass"
            else:
                result = "Fail"
            self.result_text.insert(tk.END, f"Name: {student.name}\nRoll No: {student.roll_no}\nMarks: {student.marks}\nResult: {result}\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
