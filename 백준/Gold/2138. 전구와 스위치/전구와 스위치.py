n = int(input())
s1 = list(map(int, input()))
s2 = list(map(int, input()))

for i, x in enumerate(s2):
    s1[i] ^= x
# to zero all
s3 = s1.copy()
s3[0] ^= 1
s3[1] ^= 1

inf = int(1e9)

def simulate(s1):
    cnt = 0
    for i in range(1, n):
        if s1[i - 1]:
            cnt += 1
            s1[i - 1] ^= 1
            s1[i] ^= 1
            if i + 1 < n:
                s1[i + 1] ^= 1
    if s1[-1]:
        return inf
    return cnt

ans = min(simulate(s1), simulate(s3) + 1)

if ans == inf:
    print(-1)
else:
    print(ans)