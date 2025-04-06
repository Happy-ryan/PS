n, d, k, c = map(int, input().split())
sushis = [int(input()) for _ in range(n)]

def solution(n, d, k, c, sushis):
    # 7, 9, 7, 30, 2, 7, 9, 25
    sushis = sushis + sushis
    from collections import Counter
    
    max_sushi = 0
    
    # 슬라이딩 윈도우 써보기...
    dic = Counter()
    for i in range(k):
        dic[sushis[i]] += 1
    
    for i in range(n):
        
        # 초밥개수 <- 밖에서 초기 window 셋팅
        cnt = len(dic)
        if c not in dic:
            cnt += 1
            
        # 답 갱신    
        max_sushi = max(max_sushi, cnt)
        
        # 다음 window 셋팅
        dic[sushis[i]] -= 1
        if dic[sushis[i]] == 0:
            dic.pop(sushis[i])
        dic[sushis[i + k]] += 1
        

    return max_sushi

print(solution(n, d, k, c, sushis))