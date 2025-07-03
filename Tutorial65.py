# ------------------ COMPILE-TIME POLYMORPHISM ------------------
# Python doesn't support real method overloading by default.
# But we can simulate it using default arguments or *args.

class Calculator:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print("Adding 3 values:", a + b + c)
        elif a is not None and b is not None:
            print("Adding 2 values:", a + b)
        elif a is not None:
            print("Adding 1 value:", a)
        else:
            print("No values provided.")

# Test Compile-Time (Simulated) Polymorphism
print("\n--- Compile-Time Polymorphism ---")
calc = Calculator()
calc.add(5, 10)
calc.add(2, 4, 6)
calc.add(7)
calc.add()

# ------------------ RUN-TIME POLYMORPHISM ------------------
# Achieved using Method Overriding with Inheritance

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Test Run-Time Polymorphism
print("\n--- Run-Time Polymorphism ---")
animals = [Animal(), Dog(), Cat()]
for animal in animals:
    animal.speak()
