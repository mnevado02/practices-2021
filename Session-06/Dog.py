class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name
        print("This is {}, and I'm sitting down here".format(self.name))

    def set_age(self, age):
        self.age = age


ares = Dog("ares", 10)
toby = Dog("toby", 21)
ares.set_name("trueno")
ares.set_age(1)