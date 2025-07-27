n = int(input())
qs = [list(input().split()) for _ in range(n)]

def solution(n, qs):
    
    def cal(time):
        h, m, s = time.split(":", 3)
        return int(h) * 3600 + int(m) * 60 + int(s)
    
    N =  cal('24:00:10')
    event = [0] * N
    # 미분량(변화량)을 담는 event
    # 1 2 3 4 5 6 7 8 9 10
    #     1 1 1 1
    #      1 1 1 
    # event
    #     1 0 0 0 -1  # 이벤트 누적시키기
    #      1 0 0 -1
    #     1 1 1 1 0 # 이벤트시작부터 끝 : 내 앞까의 누적 이벤트 + 현재 내 상태! 

    # 이벤트 누적시키기
    for q in qs[:-1]:
        _, s, e = q
        s, e = cal(s), cal(e)
        event[s] += 1
        event[e] += -1
    # 복구 : i번째 : event[i] += event[i - 1] 
    for i in range(1, N):
        event[i] += event[i - 1]
    
    # 윈도우의 크기에서 가장 큰 합
    W = cal(qs[-1][1])
    
    val = sum(event[:W])
    ans = val
    
    for i in range(W, N):
        val -= event[i - W]
        val += event[i]
        ans = max(ans, val)
        
    return ans
    

    
print(solution(n, qs))