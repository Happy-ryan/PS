from itertools import permutations

def f(k, tup):
    cnt = 0
    for row in tup:
        if k >= row[0]:
            k -= row[1]
            cnt += 1
        else:
            break
    return cnt

def solution(k, dungeons):
    answer = -1
    for row in list(permutations(dungeons)):
        answer = max(answer, f(k, row))
    return answer