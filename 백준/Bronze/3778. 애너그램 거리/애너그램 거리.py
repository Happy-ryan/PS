import sys
from collections import Counter
input = sys.stdin.readline

def isAnagram(standard, control):
    dic = Counter(standard)
    cnt = 0
    for x in control:
        dic[x] -= 1
        if dic[x] == 0:
            dic.pop(x)
    for x in list(dic.values()):
        cnt += abs(x)
    return cnt

n = int(input())

for i in range(n):
    standard = input()
    control = input()
    print(f"Case #{i + 1}: {isAnagram(standard, control)}")