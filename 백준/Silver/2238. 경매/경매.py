# 가장 적은 수의 사람이 제시한 가격 > 
# 이런 경우가 여럿 있다면 가장 낮은 가격으로 물건 판매 - 가장 먼저 제시한 사람에게 구매권 존재
from collections import defaultdict


u, n = map(int, input().split())
infos = [list(input().split()) for _ in range(n)]

def solution(u, n, input):
    inf = int(1e18)
    
    dic = defaultdict(list)
    for name, price in input:
        dic[int(price)].append(name)
    
    min_person = inf
    for people in dic.values():
        min_person = min(min_person, len(people))
    
    arr = list(dic.items())
    
    # 사람 적은 것 먼저 > 가격 적은 것 먼저
    arr.sort(key=lambda x : (len(x[1]), x[0]))
    
    return f"{arr[0][1][0]} {arr[0][0]}"
    
    
print(solution(u, n, infos))