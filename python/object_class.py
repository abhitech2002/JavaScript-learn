class MyClass():
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    
    def myFunc(self):
        print("Hello World "+ self.name)

p1 = Person("John", 36)
print(p1.name, p1.age)
print(p1)
p1.myFunc()

p1.age = 40
print(p1)

del p1

# print(p1)

p2 = Person("Mansi", 35)
print(p2)