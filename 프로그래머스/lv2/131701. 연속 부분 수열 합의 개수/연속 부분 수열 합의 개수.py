
# 슬라이딩 윈도우 
def solution(elements):
    answer = set()
    L = len(elements)
    elements = elements * 2                                
    for k in range(1, L + 1):
        cnt = sum(elements[0 : k])
        answer.add(cnt)
        for i in range(0, L):
            cnt -= elements[i]
            cnt += elements[i + k]
            answer.add(cnt)

    return len(answer)