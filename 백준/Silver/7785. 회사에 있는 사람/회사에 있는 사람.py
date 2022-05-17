n = int(input())
arr=[]
for _ in range(n):
    s = input().split()
    if s[1]=="enter":
        arr.append(s[0])
    else: # s[1]=="leave" 인 경우
        idx = arr.index(s[0])
        arr.pop(idx)
arr = sorted(arr)[::-1]
print(*arr, sep="\n")