import mysql.connector

class EmployeeManager:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="employee_management_system")
        self.cursor = self.conn.cursor()

    def add_employee(self, name, email, department, position):
        query = "INSERT INTO employees(name, email, department, position) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (name, email, department, position))
        self.conn.commit()

    def get_employees(self):
        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()
    
    def update_employee(self, employee_id, name, email, department, position):
        query = "UPDATE employees SET name%s,  email%s, department%s. position%s WHERE id%s"
        self.cursor.execute(query, (name, email, department, position, employee_id))
        self.cursor.commit()

    def delete_employee(self, employee_id):
        query = "DELETE FROM employees WHERE id=%s"
        self.cursor.execute(query, (employee_id,))
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()