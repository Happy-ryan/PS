n, x = map(int,input().split())
infos = [list(map(int, input().split())) for _ in range(n)]
time = 0
for s, t in infos:
    if s + t <= x:
        time = max(time, s)
if time == 0:
    print(-1)
else:
    print(time)