N = int(input())
for _ in range(N):
    arr = []
    s = input()
    for x in s:
        if len(arr) == 0:
            arr.append(x)
        else:
            if arr[-1] == x:
                continue
            else:
                arr.append(x)
    print(''.join(arr))