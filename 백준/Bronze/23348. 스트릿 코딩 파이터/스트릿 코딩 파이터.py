# https://www.acmicpc.net/problem/23348

def cal(x, y, z, a, b, c):
    return x * a + y * b + z * c

x, y, z = map(int, input().split())
n = int(input())

ans = 0
for _ in range(n):
    a1, b1, c1 = map(int, input().split())
    a2, b2, c2 = map(int, input().split())
    a3, b3, c3 = map(int, input().split())
    ans = max(ans, cal(x, y, z, a1, b1, c1) + cal(x, y, z, a2, b2, c2) + cal(x, y, z, a3, b3, c3))
    
print(ans)
    
    