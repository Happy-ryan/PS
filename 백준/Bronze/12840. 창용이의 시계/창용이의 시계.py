import sys
input = sys.stdin.readline

h, m, s = map(int, input().split())
t = int(input())
qs = [list(map(int, input().split())) for _ in range(t)]

def solution(h, m, s, qs):
    # 00시 00분 00초가 기준
    mod = 24 * 3600
    present_time = h * 3600 + m * 60 + s
    
    for q_row in qs:
        if q_row[0] == 1:
            present_time += q_row[1]
            present_time %= mod
        elif q_row[0] == 2:
            present_time += mod - q_row[1]
            present_time %= mod
        else:
            tmp = present_time
            h = tmp // 3600
            tmp %= 3600
            m = tmp // 60
            tmp %= 60
            s = tmp
            print(f"{h} {m} {s}")
            
            
solution(h, m, s, qs)