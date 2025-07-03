# ------------------ 1. Single Inheritance ------------------

class Parent:
    def show_parent(self):
        print("This is the Parent class.")

class Child(Parent):
    def show_child(self):
        print("This is the Child class (Single Inheritance).")

c = Child()
c.show_parent()
c.show_child()

# ------------------ 2. Multilevel Inheritance ------------------

class Grandparent:
    def show_grandparent(self):
        print("This is the Grandparent class.")

class Parent2(Grandparent):
    def show_parent2(self):
        print("This is the Parent class (in Multilevel Inheritance).")

class Child2(Parent2):
    def show_child2(self):
        print("This is the Child class (Multilevel Inheritance).")

c2 = Child2()
c2.show_grandparent()
c2.show_parent2()
c2.show_child2()

# ------------------ 3. Multiple Inheritance ------------------

class Father:
    def show_father(self):
        print("This is the Father class.")

class Mother:
    def show_mother(self):
        print("This is the Mother class.")

class Son(Father, Mother):
    def show_son(self):
        print("This is the Son class (Multiple Inheritance).")

s = Son()
s.show_father()
s.show_mother()
s.show_son()

# ------------------ 4. Hierarchical Inheritance ------------------

class Animal:
    def eat(self):
        print("Animal eats.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

class Cat(Animal):
    def meow(self):
        print("Cat meows.")

d = Dog()
c = Cat()
d.eat()
d.bark()
c.eat()
c.meow()

# ------------------ 5. Hybrid Inheritance ------------------

class A:
    def feature_a(self):
        print("Feature A")

class B(A):
    def feature_b(self):
        print("Feature B")

class C(A):
    def feature_c(self):
        print("Feature C")

class D(B, C):  # Inherits from B and C, both of which inherit from A
    def feature_d(self):
        print("Feature D (Hybrid Inheritance)")

d = D()
d.feature_a()
d.feature_b()
d.feature_c()
d.feature_d()

# ------------------ END OF FILE ------------------
