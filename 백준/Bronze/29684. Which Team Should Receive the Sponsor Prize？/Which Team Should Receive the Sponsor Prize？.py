while True:
    n = int(input())
    
    if n == 0:
        break
    
    times = list(map(int, input().split()))
    
    inf = int(1e18)
    min_diff = inf   # 충분히 큰 값
    answer = 0
    
    for i in range(n):
        diff = abs(times[i] - 2023)
        if diff < min_diff:
            min_diff = diff
            answer = i + 1
    
    print(answer)