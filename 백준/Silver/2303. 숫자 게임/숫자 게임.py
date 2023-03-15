# 5장 중 3장의 카드 = 5C3 = 10가지
# 브루트포스 충분히 가능하다.
from itertools import combinations
from typing import List

def cal(arr: List) -> int:
    max_num = 0
    for x1, x2, x3 in combinations(arr, 3):
        cards = x1 + x2 + x3
        cards %= 10
        max_num = max(max_num, cards)
    return max_num
        
    
n = int(input())
ans = []
for i in range(1,n + 1):
    card_arr = list(map(int, input().split()))
    ans.append((cal(card_arr), i))
    
ans.sort( key= lambda x: x[1], reverse= True)
ans.sort( key= lambda x: x[0], reverse=True)

print(ans[0][-1])
