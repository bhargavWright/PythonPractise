if __name__ == '__main__':
    n = int(input())
    student_marks = {"alekhya":[90,89,99]}

   
    for _ in range(n):
        name, *line = input().split()         alekhya 90 89 99
        scores = list(map(float, line))        
        student_marks[name] = scores
    query_name = input()
    
    l1 = student_marks[query_name]
    sum = 0 
    for k in l1:
        sum = sum + k 
    avg = sum/len(l1)
    print("%.2f"%(avg))