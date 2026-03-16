def solution(times):
    
    if times[0] == -1 and times[1] == -1 and times[2] == -1:
        return 0
    
    arr = []
    
    for idx, t in enumerate(times):
        if t == -1:
            t = 121
        arr.append((idx, t))
        
    arr.sort(key=lambda x : (x[1]))
    
    if arr[0][0] < arr[1][0] < arr[2][0]:
        return 1
    
    return 0
    
    
n = int(input())

cnt = 0
for _ in range(n):
    times = list(map(int, input().split()))
    # print(f"정답: {solution(times)}")
    cnt += solution(times)
    
print(cnt)