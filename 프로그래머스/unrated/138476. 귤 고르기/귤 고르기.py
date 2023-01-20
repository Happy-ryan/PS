from collections import Counter
def solution(k, tangerine):
    answer = 0
    ans =[]
    dic = Counter(tangerine)
    for num in sorted(dic.values(), reverse = True):
        if k > num: # k > num : num를 다 지급해도 k- num 남는다.
            k -= num
            answer += 1
        else: # k < num : 지금 num에서 k개 전부 고르기 가능 : break
            answer += 1
            break

    return answer