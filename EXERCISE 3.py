class A:
    def __str__(self):
        pass

class B(A):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "Age: " + age + ", parent: " + A.__str__






