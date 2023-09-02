class GrandParent:
    def grandparent(self):
        print("Grand Parent")
class Parent1:
    def parent1(self):
        print("Parent1")
class Parent2:
    def parent2(self):
        print("Parent2")
class Child1(GrandParent,Parent1):
    def child1(self):
        print("Child 1")
class Child2(GrandParent,Parent2):
    def Child2(self):
        print("Child 2")
o1=Child1()
o2=Child2()
o1.child1()
o1.parent1()
o1.grandparent()
o2.child2()
o2.parent2()
o2.grandparent()
