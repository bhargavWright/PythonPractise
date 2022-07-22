if __name__ == '__main__':
    l1=[]
for _ in range(int(input())):
    name=input()
    score=float(input())
    l2=[]
    l2.append(name)
    l2.append(score)
    l1.append(l2)


for i in range(len(l1)-1):
    for j in range(i+1,len(l1)):
        if(l1[i][1]<l1[j][1]):
            t=l1[i]
            l1[i]=l1[j]
            l1[j]=t
min=l1[0][1]    
t=min
for i in range(len(l1)):
    if(l1[j][1]<min):
        t=min
        min=l1[i][1]
l3=[]   
for i in range(lenl1):
    if(l1[i][1]==t):
        l3.append(l1[i][0])
    l3.sort()    
    for x in l3:
        print(x)