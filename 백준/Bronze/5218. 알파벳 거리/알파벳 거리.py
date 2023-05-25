
for _ in range(int(input())):
    a, b = input().split()
    arr = []
    for i in range(len(a)):
        if ord(a[i]) > ord(b[i]):
            arr.append(26 - (ord(a[i])-ord(b[i])))
        else:
            arr.append(ord(b[i]) - ord(a[i]))
    print("Distances:", *arr)