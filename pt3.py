class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

employees = []
    # Employee("Nguyen Van A", "Manager", 2500),
    # Employee("Tran Thi B", "Developer", 1800),
    # Employee("Le Van C", "Tester", 1500)


# emp = Employee("Le Van Tuan", "Tester", 1500)

# with open("employees.txt", "w", encoding="utf-8") as file:
#     file.write(f"{emp.name},{emp.position},{emp.salary}\n")
        

# with open("employees.txt", "w", encoding="utf-8") as file:
#     for emp in employees:
#         file.write(f"{emp.name},{emp.position},{emp.salary}\n")

with open("emp.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line == "":
            continue

        name, position, salary = line.split(",")

        employee = Employee(name, position, float(salary))
        employees.append(employee)


for emp in employees:
    print(f"{emp.name},{emp.position},{emp.salary}\n")