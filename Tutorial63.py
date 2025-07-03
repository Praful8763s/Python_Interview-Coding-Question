# ------------------ 1. Class and Object ------------------

class Student:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def display(self):  # Method
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object
s1 = Student("Praful", 23)
s1.display()

# ------------------ 2. Encapsulation ------------------

class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

# Test Encapsulation
acc = BankAccount()
acc.deposit(1000)
print("Balance:", acc.get_balance())

# ------------------ 3. Inheritance ------------------

# Single Inheritance
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

d = Dog()
d.sound()
d.bark()

# Multilevel Inheritance
class Puppy(Dog):
    def weep(self):
        print("Puppy Weeps")

p = Puppy()
p.weep()
p.bark()
p.sound()

# Multiple Inheritance
class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Art")

class Child(Father, Mother):
    def skills(self):
        print("Gaming")
        Father.skills(self)
        Mother.skills(self)

c = Child()
c.skills()

# ------------------ 4. Polymorphism ------------------

# Method Overriding (Runtime Polymorphism)
class Car:
    def start(self):
        print("Car Started")

class Tesla(Car):
    def start(self):
        print("Tesla Started Silently")

t = Tesla()
t.start()

# Method Overloading (Simulated - Compile Time Polymorphism)
class Calculator:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        elif a is not None:
            return a
        else:
            return 0

calc = Calculator()
print("Add 2 args:", calc.add(5, 10))
print("Add 3 args:", calc.add(5, 10, 15))
print("Add 1 arg :", calc.add(5))

# ------------------ 5. Abstraction ------------------

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with kick")

b = Bike()
b.start_engine()

# ------------------ END OF FILE ------------------
