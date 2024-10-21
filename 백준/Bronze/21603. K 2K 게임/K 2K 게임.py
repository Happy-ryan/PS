n, k = map(int, input().split())

def f(x):
    return x % 10

cnt = 0
ans = []
for i in range(1, n + 1):
    if f(i) != f(k) and f(i) != f(2 * k):
        cnt +=  1
        ans.append(i)
        
print(cnt)
print(*ans)