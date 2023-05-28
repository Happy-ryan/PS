import sys
input = sys.stdin.readline

t = int(input())
def f(a):
    ans = 1
    if (a & (-a)) != a:
        ans  = 0
    return ans

for _ in range(t):
    a = int(input())
    print(f(a))   