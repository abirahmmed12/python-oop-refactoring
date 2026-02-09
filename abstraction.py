from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("sleeping")

class Dog(Animal):
    def make_sound(self):
        print("ghew ghew")

class Cat(Animal):
    def make_sound(self):
        print("mew mew")

my_dog=Dog()
my_cat=Cat()
my_cat.make_sound()
my_dog.make_sound()

