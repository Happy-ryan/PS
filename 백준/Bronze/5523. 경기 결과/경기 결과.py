t = int(input())
A, B = 0,0
for _ in range(t):
    a, b = map(int,input().split())
    if a > b:
        A += 1
    elif a < b:
        B += 1

print(A, B)