n = int(input())
q = []
arr=[input().split() for _ in range(n)]
for i in range(n):
    if arr[i][0] =="push":
        q.append(arr[i][1])
    elif arr[i][0]=="pop":
        if len(q) != 0:
            print(q[0])
            q.pop(0)
        else: print("-1")
    elif arr[i][0] =="size":
        print(len(q))
    elif arr[i][0]=="empty":
        if len(q)==0:
            print("1")
        else: print("0")
    elif arr[i][0]=="front":
        if len(q) != 0:
            print(q[0])
        else: print("-1")
    else:
        if len(q) != 0:
            print(q[-1])
        else: print("-1")