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




class BasicPhne:
    def __init__(self,brand):
        self.brand=brand

    def make_call(self,number):
        print(f"{self.brand} theke {number} e call kora hocche")


class SmartPhone(BasicPhne):
    def __init__(self,brand,camera_mp):
        super().__init__(brand)
        self.camera_mp=camera_mp

    def take_photo(self):
        print(f'{self.brand} er {self.camera_mp} camera diye pic tola hocche')

phone=BasicPhne('iphone 17 pro max')

phone.make_call('343434')

phone2=SmartPhone('iphone 17 pro max',50)
phone2.take_photo()



class Product():
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def display_details(self):
        print(f"{self.name} price is {self.price}")


class Electronics(Product):
    def __init__(self, name, price,warranty_month):
        super().__init__(name, price)
        self.warranty_month=warranty_month

    def check_warranty(self):
        print(f"{self.name} has {self.warranty_month} month warranty")


class Clothing(Product):
    def __init__(self, name, price,size):
        super().__init__(name, price)
        self.size=size
    def try_on(self):
        print(f"{self.size}")


laptop = Electronics("MacBook M2", 125000, 12)


tshirt = Clothing("Polo T-Shirt", 1200, "XL")


laptop.display_details() 
laptop.check_warranty()  

print("-" * 20)

tshirt.display_details() 
tshirt.try_on()          



