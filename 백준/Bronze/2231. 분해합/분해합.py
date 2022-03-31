N = int(input())
arr =[]
for i in range(N) :
    s = i
    s += sum(map(int, str(s))) 
    if s == N :
       arr.append(i)

if len(arr) == 0 :
    print(0)
else :
    print(min(arr))