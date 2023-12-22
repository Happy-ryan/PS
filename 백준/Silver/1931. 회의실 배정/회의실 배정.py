# https://www.acmicpc.net/problem/1931
n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]


times.sort(key=lambda x: (x[1], x[0]))

cnt = 1
last_time = times[0][-1]

for start, end in times[1:]:
    if last_time <= start:
        last_time = end
        cnt += 1
        
print(cnt)