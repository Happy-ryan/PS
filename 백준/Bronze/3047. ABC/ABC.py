arr = list(map(int, input().split()))
X = input()

# A는 B보다 작고, B는 C보다 작다.
from itertools import permutations

dic = {}
for A, B, C in permutations(arr):
    if A < B and B < C:
        dic['A'] = A
        dic['B'] = B
        dic['C'] = C

for x in X:
    print(dic[x], end = ' ')