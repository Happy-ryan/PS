def solution(p, m, wants):
    seats = [0] * (m + 1)
    cnt = 0
    for want in wants:
        if seats[want] == 0:
            seats[want] = 1
        else:
            cnt += 1
            
    return cnt

t = int(input())
for _ in range(t):
    p, m = map(int, input().split())
    wants = [int(input()) for _ in range(p)]
    print(solution(p, m, wants))