class Employee():
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary


    def displaay_info(self):
        print(f"id:{self.id}| Name:{self.name} | Salary:{self.salary} TK")

    def apply_bonus(self,bonus_percentage):
        bonus=self.salary*(bonus_percentage/100)
        self.salary +=bonus
        print(f"{self.name} your salary is {self.salary}")


class Developer(Employee):
    def __init__(self, name, id, salary,language):
        super().__init__(name, id, salary)
        self.language=language

    def write_code(self):
        print(f"{self.name}is using {self.language}")

class Manager(Employee):
    def __init__(self, name, id, salary,department):
        super().__init__(name,id,salary)
        self.department=department

    def assign_task(self,task_name,employee_name):
        print(f" {self.name} '{task_name}'  {employee_name}")

dev1=Developer("Abir Chowdhury", "D101", 60000, "Python")
mngr= Manager("Rahat Ahmed", "M201", 90000, "IT Operations")

dev1.displaay_info()
mngr.displaay_info()