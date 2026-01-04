N = int(input())
infos = [list(map(int, input().split())) for _ in range(N)]

def solution(N, infos):
    
    high = 0
    for info in infos:
        A, B = info
        high += A
        high -= B
        print(high)
        
solution(N, infos)