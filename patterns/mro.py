class Parent():
    def parent_method(self):
        print("First parent class")


class Parent2(Parent):
    pass
    # def parent_method(self):
    #     print("Second parent class")


class Parent3(Parent):
    def parent_method(self):
        print("Third parent class")


class Child(Parent2, Parent3):
    def child_method(self):
        print("The child method")


parent2 = Parent2()
parent2.parent_method()
child = Child()
child.parent_method()
print(Child.mro())