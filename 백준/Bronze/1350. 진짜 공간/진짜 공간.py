n = int(input())
files = list(map(int, input().split()))
cluster = int(input())

def solution(n, files, cluster):
    cnt = 0
    
    for f in files:
        cnt += f // cluster
        if f % cluster != 0:
            cnt += 1
            
    return cnt * cluster

print(solution(n, files, cluster))