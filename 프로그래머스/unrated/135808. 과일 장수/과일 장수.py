# 그리디 - 정렬(난이도 하)
def solution(k, m, score):
    # print(list(reversed(sorted(score))))
    # m만큼 리스트를 슬라이싱함 m = 4 > 0:4(0123)
    answer = 0    
    score = list(reversed(sorted(score)))
    for i in range(0, len(score), m ):
        arr = score[i: i+m]
        if len(arr) == m:
            answer += min(arr) * m            
    return answer