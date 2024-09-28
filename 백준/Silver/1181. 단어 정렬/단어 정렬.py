n = int(input())
# 중복제거
words = list(set(list(input() for _ in range(n))))

from functools import cmp_to_key

def solution(n: int, words: list[str]):
    # 1. 길이가 짧은 것 > 길이 기준 오름차순
    # 2. 길이가 같으면 사전순 > 단어 기준 오름차순
    # 단, 중복은 하나만 남기고 제거

    # 정렬의 우선순위가 2개이상일 경우 가장 후순위정렬부터 시작!
    # 1) 사전순으로 먼저 정렬
    words.sort()
    # 2) 길이순 정렬
    def compare(word1, word2):
        x = len(word1)
        y = len(word2)
        if x == y:
            return 0
        if x - y < 0:
            return -1
        if x - y > 0:
            return 1
    words.sort(key=cmp_to_key(compare))
    
    for word in words:
        print(word)
        
def solution2(n, words):
    words.sort(key = lambda x: (len(x), x)) # (정렬1순위, 2순위)
    for word in words:
        print(word)


solution2(n, words)