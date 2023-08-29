class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def _str_(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

class EmployeeTable:
    def _init_(self, employees):
        self.employees = employees 

    def search(self, parameter):
        if parameter == 1:
            return sorted(self.employees, key=lambda x: x.age)
        elif parameter == 2:
            return sorted(self.employees, key=lambda x: x.name)
        elif parameter == 3:
            operator = input("Enter operator (<, >, <=, >=): ")
            value = int(input("Enter value: "))
            if operator == "<":
                return [emp for emp in self.employees if emp.salary < value]
            elif operator == ">":
                return [emp for emp in self.employees if emp.salary > value]
            elif operator == "<=":
                return [emp for emp in self.employees if emp.salary <= value]
            elif operator == ">=":
                return [emp for emp in self.employees if emp.salary >= value]
            else:
                raise ValueError("Invalid operator")

if _name_ == "_main_":
    employees = [
        Employee ("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]
    table = EmployeeTable(employees)
    print("Select a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    parameter = int(input("Enter your choice: "))
    results = table.search(parameter)
    print("\nSearch results:")
    for result in results:
        print(result)