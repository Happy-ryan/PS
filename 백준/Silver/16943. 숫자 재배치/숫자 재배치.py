# https://www.acmicpc.net/problem/16943

A, B = map(int,input().split())
arr = list(str(A))
ans = []
used = [0] * len(arr)
C = -1

def caluclate():
    sum_val = 0
    for idx, number in enumerate(ans):
        if idx == 0 and int(number) == 0:
            return -1
        sum_val += int(number) * 10**(len(ans) - idx - 1)
    return sum_val

def back(level):
    global B, C
    if level == len(arr):
        k = caluclate()
        if k < B:
            C = max(C, k)
        return
    
    for i in range(len(arr)):
        if used[i] == 0:
            used[i] = 1
            ans.append(arr[i])
            back(level+1)
            ans.pop()
            used[i] = 0
        
back(0)

print(C)