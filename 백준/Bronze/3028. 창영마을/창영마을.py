s = input()
arr = [1, 0, 0]
for i in s :
    if i =="A" :
        arr[0],arr[1]=arr[1],arr[0]
    elif i == "B" :
        arr[1],arr[2]=arr[2],arr[1]
    else :
        arr[0],arr[2]=arr[2],arr[0]

if arr[0] == 1 :
    print(1)
elif arr[1] == 1 :
    print(2)
else :
    print(3)