# https://www.acmicpc.net/problem/28289
N = int(input())
ans = [0] * 4

def chcek(a, b):
    if a == 1:
        return 3
    else:
        if b == 1 or b == 2:
            return 0
        elif b == 3:
            return 1
        else:
            return 2
        
for _ in range(N):
    a, b, c = map(int, input().split())
    ans[chcek(a, b)] += 1
    
for x in ans:
    print(x)