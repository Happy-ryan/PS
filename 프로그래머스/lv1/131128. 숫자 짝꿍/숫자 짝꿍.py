from collections import Counter
def solution(X, Y):
    answer = ''
    X_dict = Counter(X)
    Y_dict = Counter(Y)
    
    for key in range(9, -1, -1):
        answer += min(X_dict[str(key)], Y_dict[str(key)]) * str(key) 

    if len(answer) == 0:
        return '-1'
    elif answer[0] == '0' :
        return '0'
    else:
        return answer