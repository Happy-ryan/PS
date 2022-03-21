n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    sum = 0
    for j in range (1,int(arr[0])+1) :
        sum = sum + arr[j]
    aver = sum / (arr[0])
    stu = 0
    for k in range(1,int(arr[0])+1) :
        if arr[k] > aver :
            stu += 1 
    
    print("%.3f%%" %((stu/arr[0])*100))   