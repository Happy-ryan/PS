n, d, k, c = map(int, input().split())
sushis = [int(input()) for _ in range(n)]

def solution(n, d, k, c, sushis):
    # 7, 9, 7, 30, 2, 7, 9, 25
    sushis = sushis + sushis
    from collections import Counter
    
    max_sushi = 0
    
    dic = Counter()
    idx = 0
    while idx < n:
        if idx == 0:
            for i in range(idx, idx + k):
                dic[sushis[i]] += 1
        else:
            dic[sushis[idx - 1]] -= 1
            if dic[sushis[idx - 1]] == 0:
                dic.pop(sushis[idx - 1])
            dic[sushis[idx + k - 1]] += 1
        
        # print(f"idx: {idx}, sushi: {dic}")
        
        if c in dic:
            max_sushi = max(max_sushi, len(dic.keys()))
        else:
            max_sushi = max(max_sushi, len(dic.keys()) + 1)
        
        idx += 1

    return max_sushi

print(solution(n, d, k, c, sushis))