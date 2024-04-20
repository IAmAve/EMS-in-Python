import tkinter as tk
from tkinter import messagebox

from employee import EmployeeManager

class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("EMPLOYEE SYSTEM MANAGEMENT")
        self.emp_manager =  EmployeeManager()


        self.create_gui()

    def create_gui(self):
        #FOR LABELING ONLY
        tk.Label(self.master, text="Name: ").grid(row=0, column=0, sticky="e")
        tk.Label(self.master, text="Email: ").grid(row=1, column=0, sticky="e")
        tk.Label(self.master, text="Department: ").grid(row=2, column=0, sticky="e")
        tk.Label(self.master, text="Position: ").grid(row=3, column=0, sticky="e")

        #ENTRY FIELDS
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=1, column=1)
        self.department_entry = tk.Entry(self.master)
        self.department_entry.grid(row=2, column=1)
        self.position_entry = tk.Entry(self.master)
        self.position_entry.grid(row=3, column=1)

        #CLICK BUTTON
        tk.Button(self.master, text="Add Employee", command=self.add_employee).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Show Employee", command=self.show_employee).grid(row=6, column=0, columnspan=2, pady=10)

    #FOR VALIDATIONS
    def add_employee(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        department = self.department_entry.get()
        position = self.position_entry.get()

        if name and email and department and position:
            self.emp_manager.add_employee(name, email, department, position)
            messagebox.showinfo("SUCCESS!!, Employee Added Successfully")
        else:
            messagebox.showinfo("ERROR ><, No Employees Found")

    def show_employee(self):
        employees = self.emp_manager.get_employees()

        if employees:
            for employee in employees:
                print(employee)
        else:
            messagebox.showinfo("INFO, No Employees Found")

def main():
    root = tk.Tk()
    app = EmployeeGUI(root)
    root.mainloop()

if __name__=="__main__":
    main()