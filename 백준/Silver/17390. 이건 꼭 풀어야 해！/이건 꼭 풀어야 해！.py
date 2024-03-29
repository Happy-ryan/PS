import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = [0] + sorted(list(map(int, input().split())))
psum = [0] * (n + 1)
for i in range(1, n + 1):
    psum[i] = psum[i - 1] + arr[i]

def sub_sum(l, r, psum):
    cnt = psum[r] - psum[l - 1]
    return cnt

for _ in range(q):
    l, r = map(int, input().split())
    print(sub_sum(l,r, psum))