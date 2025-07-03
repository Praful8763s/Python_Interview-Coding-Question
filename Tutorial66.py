# Sure! Below is a **Python program** that demonstrates \*\*all types of **access specifiers** and **identifiers** in a single code example using OOPs concepts.

# ---

# ### ✅ Concepts Covered:

# | Concept              | Shown in Code                                               |
# | -------------------- | ----------------------------------------------------------- |
# | Public Identifier    | Normal attribute/method (`name`)                            |
# | Protected Identifier | `_balance`                                                  |
# | Private Identifier   | `__password`                                                |
# | Access Specifiers    | public, protected, private (by naming convention in Python) |
# | OOP Concept          | Class, Object, Encapsulation, Inheritance                   |

# ---

# ### 🐍 Python Code: Access Specifiers + Identifiers with OOP

# ```python
class User:
    def __init__(self, name, balance, password):
        self.name = name                # Public Identifier
        self._balance = balance         # Protected Identifier
        self.__password = password      # Private Identifier

    # Public Method
    def show_user(self):
        print(f"User: {self.name}")
        print(f"Balance (Protected): {self._balance}")
        print(f"Password (Private): {self.__password}")

    # Getter for private variable
    def get_password(self):
        return self.__password

    # Setter for private variable
    def set_password(self, new_password):
        self.__password = new_password

# Inherited class to test access
class Admin(User):
    def __init__(self, name, balance, password):
        super().__init__(name, balance, password)

    def access_protected(self):
        print(f"Admin accessing protected balance: {self._balance}")

    def try_private_access(self):
        try:
            print(f"Trying to access private password: {self.__password}")
        except AttributeError:
            print("Cannot access private variable __password directly!")


# Create Object
print("--- Creating User Object ---")
u = User("Praful", 10000, "secret123")
u.show_user()

print("\n--- Access from Outside the Class ---")
print("Public:", u.name)
print("Protected:", u._balance)  # Possible, but not recommended
# print("Private:", u.__password)  # Uncommenting this line will raise an error
print("Private (via getter):", u.get_password())

print("\n--- Using Admin (Subclass) ---")
admin = Admin("Admin", 9999, "admin@123")
admin.access_protected()
admin.try_private_access()
# ```

# ---

# ### 🔐 Access Specifiers in Python

# | Specifier | Naming Syntax | Access Level                                                        |
# | --------- | ------------- | ------------------------------------------------------------------- |
# | Public    | `name`        | Accessible everywhere                                               |
# | Protected | `_balance`    | Accessible in class and subclass                                    |
# | Private   | `__password`  | Accessible only inside the class (`_ClassName__password` if forced) |

# ---

# ### 📌 Output Summary:

# ```text
# --- Creating User Object ---
# User: Praful
# Balance (Protected): 10000
# Password (Private): secret123

# --- Access from Outside the Class ---
# Public: Praful
# Protected: 10000
# Private (via getter): secret123

# --- Using Admin (Subclass) ---
# Admin accessing protected balance: 9999
# Cannot access private variable __password directly!
# ```

# ---

# Would you like this example in **Java** or **C++**, where access specifiers (`public`, `private`, `protected`) are enforced explicitly?
