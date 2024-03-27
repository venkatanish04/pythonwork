'''class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of Rs.{amount} successful")
        else:
            print("Invalid deposit amount.")

    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of Rs.{amount} successful.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    def bank_fees(self):
        fees=0.05*self.balance
        self.balance-=fees
        print(f"Bank fees of Rs.{fees}applied")
    def display(self):
        print(f"Account Number:{self.accountNumber}")
        print(f"Account Holder:{self.name}")
        print(f"balance:{self.balance}")


account1 = BankAccount(123456, "John Doe", 1000)
account1.display()
account1.deposit(500)
account1.withdrawal(200)
account1.bank_fees()
account1.display()


class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def display_namespaces(self):
        print("Class namespaces:")
        print(dir(MyClass))
        print("\nInstance namespaces:")
        print(dir(self))


# Creating an instance of the class
obj = MyClass("I am an instance variable")

# Displaying namespaces
obj.display_namespaces()

class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_attributes(self):
        print("Attributes and their values:")
        for attr, value in vars(self).items():
            print(f"{attr}: {value}")

    def remove_attribute(self, attribute_name):
        if hasattr(self, attribute_name):
            delattr(self, attribute_name)
            print(f"{attribute_name} attribute removed.")
        else:
            print(f"{attribute_name} attribute not found.")
student1 = Student(student_id=1, student_name="John Doe", student_class="10A")
student1.display_attributes()
student1.new_attribute = "New Value"
print("\nAfter adding a new attribute:")
student1.display_attributes()
student1.remove_attribute("student_name")
print("\nAfter removing the student name attribute:")
student1.display_attributes()
'''