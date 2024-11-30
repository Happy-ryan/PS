n = int(input())
ans = [input() for _ in range(n)]
ps = [input() for _ in range(n)]

cnt = 0
for idx in range(n):
    if ans[idx] == ps[idx]:
        cnt += 1
print(cnt)