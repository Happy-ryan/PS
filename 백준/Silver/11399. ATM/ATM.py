N = int(input())
times = sorted(list(map(int,input().split())))

cnt = 0
for i  in range(len(times)):
    cnt += sum(times[:i+1])
print(cnt)