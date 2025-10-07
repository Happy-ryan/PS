t = int(input())

from itertools import combinations

def solution(n, words):
    
    for w1, w2 in combinations(words, 2):
        t1 = w1 + w2
        t2 = w2 + w1
        if t1 == t1[::-1]:
            return t1
        if t2 == t2[::-1]:
            return t2
    return 0

for _ in range(t):
    n = int(input())
    words = [input() for _ in range(n)]
    print(solution(n, words))