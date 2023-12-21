# https://www.acmicpc.net/problem/2841
from collections import defaultdict
n, p = map(int, input().split())
# 각 줄은 독립적!
guitar_strings_melody = defaultdict(list)

for _ in range(n):
    string_number, plat_number = map(int, input().split())
    guitar_strings_melody[string_number].append(plat_number)
    
def count_finger_number(plats):
    stack = []
    cnt = 0

    for plat in plats:
        # 새로운 plat이 stack에 마지막이 될 때까지 pop
        while stack and stack[-1] > plat:
            stack.pop()
            cnt += 1
        # stack이 비어있거나 새로운 plat이 가장 큰 경우        
        if not stack or stack[-1] < plat:
            stack.append(plat)
            cnt += 1

    return cnt

ans = 0
for key in guitar_strings_melody.keys():
    ans += count_finger_number(guitar_strings_melody[key])
print(ans)