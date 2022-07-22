# write a prog to print the given digit is one digit or two digit or more than three

n=int(input("enter a value"))
if(n<10):
    print("The given num is one digit")
elif(n<99):
    print("The given num is two digit")
elif(n<999):
    print("the given num is three digit")
else:
    print("the num is a four digit")
