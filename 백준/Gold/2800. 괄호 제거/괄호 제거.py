#https://www.acmicpc.net/problem/2800
#시간복잡도: O(2^10 - 1) -> brute force
# 괄호는 stack...

from itertools import combinations

s = list(input())
stack = []
pairs = []
for idx, x in enumerate(s):
    # 여는 괄호는 반드시 들어가고
    if x == '(':
        stack.append(('(', idx))
    elif x == ')':
        # 닫는 괗호가 나왔는데 -1이 여는 괄호라면 pair로 연결시키고 stack에서 pop
        if len(stack) and stack[-1][0] == '(':
            pairs.append((stack[-1][1], idx))
            stack.pop()
        else:
            raise "Fuckyou"

# 서로 다른 식
# 연속된 괄호의 경우 중복가능 (((0+0)))
ans = set()
for  i in range(1, len(pairs) + 1):
    for row in combinations(pairs, i):
        arr = s.copy()
        for x, y in row:
            arr[x] = ''
            arr[y] = ''
        ans.add(''.join(arr))
        
ans = sorted(list(ans))

for x in ans:
    print(x)       
