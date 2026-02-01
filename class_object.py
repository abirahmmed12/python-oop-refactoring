class Laptop:
    def __init__(self,brand,ram,processor):
        self.brand=brand
        self.ram=ram
        self.processor=processor
        self.is_on= False

    
    def start(self):
        if not self.is_on:
            self.is_on=True
            print(f'{self.brand} is being on')
        else:
            print(f"{self.brand} is already on")

    def run_code(self):
        if self.is_on:
            print(f"code has been run succesfullly and {self.ram} and {self.processor}working succesfully")

        else:
            print(f"please open {self.brand} first")

    def shutdown(self):
        if self.is_on:
            self.is_on=False
            print(f'{self.brand} has been succesfully shutdown')
        else:
            print(f"{self.brand}is alreday shutdown")


my_laptop=Laptop('Mac book','Asus 16GB Ram','Ryzon 7')
my_laptop.start()
my_laptop.run_code()
my_laptop.shutdown()

