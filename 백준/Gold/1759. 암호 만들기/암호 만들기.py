import sys
from collections import Counter

input = sys.stdin.readline

L, C = map(int, input().split())
arr = sorted(list(input().split()))

used = [0] * C
visited = [-1]
num = []

def dfs(lev):

    if lev == L:
        if Counter(num)['a'] + Counter(num)['e'] + Counter(num)['i'] + Counter(num)['o'] + Counter(num)['u'] >= 1 and\
            Counter(num)['b'] + Counter(num)['c'] + Counter(num)['d'] + Counter(num)['f'] + Counter(num)['g'] + Counter(num)['h'] +\
                Counter(num)['j'] + Counter(num)['k'] + Counter(num)['l'] + Counter(num)['m'] + Counter(num)['n'] + Counter(num)['p'] +\
                    Counter(num)['q'] + Counter(num)['r'] + Counter(num)['s'] + Counter(num)['t'] + Counter(num)['w'] + Counter(num)['x'] +\
                        Counter(num)['y'] + Counter(num)['z'] >= 2:
                        print(''.join(num))
                        return
    
    for i in range(visited[-1] + 1, len(arr)):
        if used[i] == 0:
            visited.append(i)
            used[i] = 1
            num.append(arr[i])
            dfs(lev + 1)
            num.pop()
            used[i] = 0
            visited.pop()

dfs(0)