import csv
import tkinter as tk
from tkinter import messagebox, simpledialog

class Employee:
    def __init__(self, id, name, dob, hire_date, department, job_title, salary):
        self.id = id
        self.name = name
        self.dob = dob
        self.hire_date = hire_date
        self.department = department
        self.job_title = job_title
        self.salary = salary

class EmployeeManagementSystem:
    def __init__(self, filename):
        self.filename = filename
        self.employees = self.load_employees()
        self.root = tk.Tk()
        self.root.title("Employee Management System")
        self.create_gui()

    def load_employees(self):
        employees = []
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        employee = Employee(int(row[0]), row[1], row[2], row[3], row[4], row[5], float(row[6]))
                        employees.append(employee)
        except FileNotFoundError:
            pass
        return employees

    def save_employees(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for employee in self.employees:
                writer.writerow([employee.id, employee.name, employee.dob, employee.hire_date, employee.department, employee.job_title, employee.salary])

    def add_employee(self, name, dob, hire_date, department, job_title, salary):
        employee = Employee(len(self.employees) + 1, name, dob, hire_date, department, job_title, float(salary))
        self.employees.append(employee)
        self.save_employees()

    def retrieve_employee(self, id):
        for employee in self.employees:
            if employee.id == int(id):
                return employee
        return None

    def update_employee(self, id, name, dob, hire_date, department, job_title, salary):
        for employee in self.employees:
            if employee.id == int(id):
                employee.name = name
                employee.dob = dob
                employee.hire_date = hire_date
                employee.department = department
                employee.job_title = job_title
                employee.salary = float(salary)
        self.save_employees()

    def create_gui(self):
        self.root.configure(bg='#f0f0f0')

        frame = tk.Frame(self.root, bg='#e0e0e0', pady=10, padx=10)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="Employee Management System", font=('Helvetica', 16), bg='#e0e0e0').grid(row=0, column=0, columnspan=2, pady=10)

        self.name_entry = self.create_label_entry(frame, "Name:", 1)
        self.dob_entry = self.create_label_entry(frame, "DOB:", 2)
        self.hire_date_entry = self.create_label_entry(frame, "Hire Date:", 3)
        self.department_entry = self.create_label_entry(frame, "Department:", 4)
        self.job_title_entry = self.create_label_entry(frame, "Job Title:", 5)
        self.salary_entry = self.create_label_entry(frame, "Salary:", 6)

        tk.Button(frame, text="Add Employee", command=self.add_employee_gui, bg='#4CAF50', fg='white').grid(row=7, column=0, pady=10)
        tk.Button(frame, text="Retrieve Employee", command=self.retrieve_employee_gui, bg='#2196F3', fg='white').grid(row=7, column=1, pady=10)

        self.root.mainloop()

    def create_label_entry(self, parent, text, row):
        label = tk.Label(parent, text=text, bg='#e0e0e0')
        label.grid(row=row, column=0, sticky='e', padx=5, pady=5)
        entry = tk.Entry(parent)
        entry.grid(row=row, column=1, padx=5, pady=5)
        return entry

    def add_employee_gui(self):
        name = self.name_entry.get()
        dob = self.dob_entry.get()
        hire_date = self.hire_date_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        salary = self.salary_entry.get()
        self.add_employee(name, dob, hire_date, department, job_title, salary)
        messagebox.showinfo("Success", "Employee added successfully")

    def retrieve_employee_gui(self):
        id = simpledialog.askinteger("Retrieve Employee", "Enter Employee ID")
        employee = self.retrieve_employee(id)
        if employee:
            info = (f"ID: {employee.id}\n"
                    f"Name: {employee.name}\n"
                    f"DOB: {employee.dob}\n"
                    f"Hire Date: {employee.hire_date}\n"
                    f"Department: {employee.department}\n"
                    f"Job Title: {employee.job_title}\n"
                    f"Salary: {employee.salary}")
            messagebox.showinfo("Employee Details", info)
        else:
            messagebox.showerror("Error", "Employee not found")

if __name__ == "__main__":
    ems = EmployeeManagementSystem('employees.csv')