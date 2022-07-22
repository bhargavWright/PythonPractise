# memory does not allocate to the class members
class Emp:

    # method 

    def accept(self):

        self.eno = int(input("Enter the empno"))
        self.ename =input("Entr the ename")
        self.esal =float(input("Enter the emp sal"))
    def display(self):
        print(self.eno," ",self.ename," ",self.esal)

# when ever we have create an object to the class 

# how to create an object


e1 = Emp()
e2 = Emp()    
e3 = Emp()

e1.accept()
e2.accept()
e3.accept()

e1.display()
e2.display()
e3.display()








