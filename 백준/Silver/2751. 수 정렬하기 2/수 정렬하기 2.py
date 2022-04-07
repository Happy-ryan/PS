N = int(input())
arr = []
for _ in range(N) :
    num = int(input()) 
    arr.append(num) 
sort_list = sorted(arr) 
for i in sort_list : 
    print(i)
