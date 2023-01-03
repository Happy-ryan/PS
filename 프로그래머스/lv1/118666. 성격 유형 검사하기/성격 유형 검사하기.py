from collections import Counter

def f(arr, choice): # 성격유형과 동의비동의에 따른 점수
    scores = [0, (arr[0], 3),(arr[0], 2),(arr[0], 1),(arr[0],0),\
                (arr[1], 1),(arr[1], 2),(arr[1], 3)]
    
    return scores[choice][0], scores[choice][1]

def solution(survey, choices):
    answer = ''
    score_dict = Counter()
    for k in range(len(survey)):
        p = f(survey[k],choices[k])[0]
        q = f(survey[k],choices[k])[1]
        score_dict[p] += q
        
    # 'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T' 사전식 
    
    for i, j in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        if score_dict[i] < score_dict[j]:
            answer += j
        else:
            answer += i
        
    return answer