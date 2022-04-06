arr= list(map(int, input().split()))
ret1 = 0
ret2 = 0
for i in range(7) :
    if arr[i+1] - arr[i] == 1 :
        ret1 +=1
    elif arr[i]-arr[i+1] == 1:
        ret2 +=1
if ret1 ==7 :
    print("ascending")
elif ret2 == 7 :
    print("descending")
else :
    print("mixed")