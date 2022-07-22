a=input("enter any character")
if(ord(a>=65 and a<=90)):
    print(a," is a upper case")
elif(ord(a>=97 and a<=123)):
    print(a," is a lower case")
elif(ord(a>=48 and a<=57)):
    print(a,"is a num")
else:
    print(a,"is a special character")