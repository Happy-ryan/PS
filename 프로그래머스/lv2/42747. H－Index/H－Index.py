def solution(citations):
    answer = 0
    citations.sort()
    for h in range(0, citations[-1] + 1):
        cnt = 0
        for cite in citations:
            if cite > h:
                cnt += 1
        print(cnt)
        if h == cnt:
            answer = max(answer, h)
        
    return answer