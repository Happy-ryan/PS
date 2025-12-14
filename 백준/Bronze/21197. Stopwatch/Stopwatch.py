n = int(input())
times = [int(input()) for _ in range(n)]

def solution(n, times):
    
    val = 0
    
    if n % 2 != 0:
        return 'still running'
    else:
        for i in range(1, n, 2):
            val += times[i] - times[i - 1]
    
    return val

print(solution(n, times))