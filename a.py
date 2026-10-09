class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

s1 = Student("Rahim", 18)
s1.show()