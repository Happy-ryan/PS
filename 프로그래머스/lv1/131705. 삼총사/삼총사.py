from itertools import combinations
def solution(number):
    answer = 0
    for x, y, z in combinations(number, 3):
        if x + y + z == 0:
            answer += 1
    return answer