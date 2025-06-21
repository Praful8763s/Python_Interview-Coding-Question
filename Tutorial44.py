# Access Specifier in Python OOPS Concept
# Public Access Specifier
class Public:
    def __init__(self):
        self.name ="John"
        self.age = 30
    def display_age(self):
        print(self.name)
        print(self.age)
obj = Public()
obj.display_age()

#Private Access Specifier using Python
class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def salary(self):
        return self.__salary  # Access through public method

obj = Private()
print(obj.salary())  # Works
#print(obj.__salary)  # Raises AttributeError
# inner classs 
class Color:

    # constructor method

    def __init__(self):

        # object attributes

        self.name = 'Green'
        self.lg = self.Lightgreen()

    def show(self):
        print('Name:', self.name)


	# create Inner Lightgreen class

    class Lightgreen:

        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'

        def display(self):
            print('Name:', self.name)
            print('Code:', self.code)

# create Color class object
outer = Color()


# method calling
outer.show()

# create a Lightgreen
# inner class object

g = outer.lg

# inner class method calling

g.display()
