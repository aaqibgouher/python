class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_details(self):
        print(self.name)
        print(self.age)
    
    def greeting(self, greet):
        print(greet+" "+self.name)

s = Student("nazish", 25)
s.print_details()
s.greeting("hello")