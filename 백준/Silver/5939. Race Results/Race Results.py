n = int(input())
hours = [list(map(int, input().split())) for _ in range(n)]

def solution(n, hours):
    hours.sort(key= lambda x: (x[0], x[1], x[2]))
    
    for hour in hours:
        print(*hour)
        
solution(n, hours)