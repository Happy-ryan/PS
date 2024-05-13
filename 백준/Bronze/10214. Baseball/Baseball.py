def solution(infos):
    y_score_total = 0
    k_score_total = 0
    
    for info in infos:
        y_score, k_score = info
        y_score_total += y_score
        k_score_total += k_score
    
    if y_score_total > k_score_total:
        return 'Yonsei'
    elif y_score_total < k_score_total:
        return 'Korea'
    else:
        return 'Draw'

t = int(input())

for _ in range(t):
    infos = [list(map(int, input().split())) for _ in range(9)]
    print(solution(infos))