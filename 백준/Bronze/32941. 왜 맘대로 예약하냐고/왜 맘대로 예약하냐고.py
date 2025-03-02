t, x = map(int, input().split())
n = int(input())
flag = True

for _ in range(n):
    k = int(input())
    A = list(map(int, input().split()))

    if x not in A:
        flag = False
        
print('YES' if flag else 'NO')