n, q = map(int, input().split())
arr = [0] * (n + 1)
for _ in range(q):
    L, I = map(int, input().split())
    for i in range(L, n + 1, I):
        arr[i] = 1
        
print(n - sum(arr[1:]))