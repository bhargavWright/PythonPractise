class Book:

    def getData(self):
        self.bname = input("Enter the bname")
        self.bcost = float(input("enter the price"))
        self.bauthor = input("Enter the author")
    
    def putData(self):
        print("==========================")
        print(self.bname," ",self.bcost," ",self.bauthor)
        

b1  = Book()

b1.getData()
b1.putData()
