from collections import Counter
def solution(k, tangerine):
    answer = 0
    ans =[]
    for key, value in Counter(tangerine).items():
        ans.append((value, key)) # (귤의 갯수, 귤의 종류)
    ans.sort( key = lambda x : x[0], reverse = True)
    for num, _ in ans:
        if k > num:
            k -= num
            answer += 1
        else: # k < num : 지금 num에서 k개 전부 고르기 가능 : break
            answer += 1
            break

    return answer