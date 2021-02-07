class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name + " is ", self.age + " years old")


x = Animal("Zebra", "19")
x.printname()


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.bestfood = "Hotdog"


x = Dog("Sizza", "18")
x.printname()


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.color = "Brown"


y = Cat("Bob", "8")
y.printname()
