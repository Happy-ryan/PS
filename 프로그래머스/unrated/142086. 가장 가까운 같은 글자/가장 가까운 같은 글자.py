from collections import defaultdict
def solution(s):
    answer = []
    dic = defaultdict(list)
    for i, x in enumerate(s):
        if len(dic[x]) == 0: # 처음 나왔다면 answer -1 삽입
            answer.append(-1)
        else:
            k = i - dic[x][-1] # 이미 나왔다면 키의 밸류 - list 중 가장 가까운 인덱스와의 차이를 answer에 삽입
            answer.append(k)
        dic[x].append(i) # ket 가 x 인 것의 밸류리스트에 삽입

    return answer