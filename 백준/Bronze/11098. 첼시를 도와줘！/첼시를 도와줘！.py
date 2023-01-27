from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    dic = defaultdict()
    for _ in range(n):
        a, b = input().split()
        dic[int(a)] = b
    print(dic[max(dic.keys())])