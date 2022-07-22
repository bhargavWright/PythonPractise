class Student:

    def __init__(self,sno,sname,scourse,sfee):
        self.sno = sno
        self.sname = sname
        self.scourse = scourse
        self.sfee = sfee
    
    def display(self):
        print(self.sno," ",self.sname," ",self.scourse," ",self.sfee)

s1 = Student(101,"ram","c",3000)
s2 = Student(102,"sita","cpp",4000)

s1.display()
s2.display()
    
