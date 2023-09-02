class Parent1:
    def displayP1(self):
        print("this is Parent class")

class Parent2:
    def displayP2(self):
        print("this is Parent class")

class Parent3:
    def displayP3(self):
        print("this is Parent class")

class Child1(Parent1,Parent2,Parent3):
    def displayP(self):
        print("this is Child class")
#multiple inheritance
o1=Child1()
o1.displayP1()
o1.displayP2()
o1.displayP3()
