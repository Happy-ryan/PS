import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
words = [input() for _ in range(n)]
f_word = words[0]
answer = 0

def isPeudoAnagram(s1, s2):
    flag = False
    dic = Counter()

    for x1 in s1:
        dic[x1] += 1

    for x2 in s2:
        dic[x2] -= 1
        if dic[x2] == 0:
            dic.pop(x2) # 0을 삭제하므로 애너그램의 경우 빈 리스트만 남는다.
    
    if list(dic.values()) in [[-1], [1], [], [-1, 1], [1, -1]]:
        flag = True

    return flag
    
for word in words[1:]:
    if isPeudoAnagram(f_word, word):
        answer += 1

print(answer)