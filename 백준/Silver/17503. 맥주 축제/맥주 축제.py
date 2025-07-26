# N일동인 K개의 종류의 맥주 중 N개의 맥주 섭취
# 섭취했던 맥주는 재섭취 불가
# 섭취할 N개 맥주의 선호도의 합 >= M
# 전씨의 간 레벨 < 맥주 도수 : 기절 엔딩

# 선호도의 합 M을 채우면서 N개의 맥주를 모두 마실 수 있는 간 레벨의 최솟값
# 불가하면 -1

N, M, K = map(int, input().split())
beers = [list(map(int, input().split())) for _ in range(K)]


def solution(N, M, K, beers):
    
    # 정렬 : 선호도 큰 것부터 뽑아야함
    beers.sort(key=lambda x : -x[0])
    
    def cal(level):
        val = 0
        cnt = 0
        # print(beers)
        for v, c in beers:
            if cnt == N:
                break
            if c <= level:
                val += v
                cnt += 1
        if cnt < N:
            return 0
        return val

    inf = pow(2, 31) + 1
    l, r = 0, inf
    while l <= r:
        m = (l + r) // 2
        # print(m, cal(m))
        if cal(m) >= M:
            r = m - 1
        else:
            l = m + 1
            
    if r == inf:
        return -1

    return l
        
        

print(solution(N, M, K, beers))