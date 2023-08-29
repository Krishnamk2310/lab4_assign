class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def _init_(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, target_age):
        results = []
        for emp in self.employees:
            if emp.age == target_age:
                results.append(emp)
        return results

    def search_by_name(self, target_name):
        results = []
        for emp in self.employees:
            if emp.name.lower() == target_name.lower():
                results.append(emp)
        return results

    def search_by_salary(self, operator, target_salary):
        results = []
        for emp in self.employees:
            if operator == '>' and emp.salary > target_salary:
                results.append(emp)
            elif operator == '<' and emp.salary < target_salary:
                results.append(emp)
            elif operator == '>=' and emp.salary >= target_salary:
                results.append(emp)
            elif operator == '<=' and emp.salary <= target_salary:
                results.append(emp)
        return results

def main():
    emp_table = EmployeeTable()

    emp_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search Parameters:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (> < <= >=)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        target_age = int(input("Enter target age: "))
        results = emp_table.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter target name: ")
        results = emp_table.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter operator (> < <= >=): ")
        target_salary = int(input("Enter target salary: "))
        results = emp_table.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice!")
        return

    if results:
        print("\nSearch Results:")
        for emp in results:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No matching results found.")

if _name_ == "_main_":
    main()