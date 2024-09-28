n = int(input())
dists = list(int(input()) for _ in range(n))

def solution(n, dists):
    # 원주
    total_dist = sum(dists)
    
    # 원형
    dists += dists
    
    # 두 점 사이의 거리 - 누적합
    psum = [0] * (2 * n + 1)
    for i in range(2 * n - 1):
        psum[i + 1] = dists[i] + psum[i]
    
    # 같은 방향 투포인터..?
    ans = 0
    r = 1
    for l in range(n):
        # 다음거리가 절반을 넘는지 확인하는 절차
        # 소수점 이슈는 반대편에 곱하기로!
        
        # 기존의 조건만 존재하면 l은 계속 커지는데 r이 커지지 않는 경우가 있을 수도 있다.
        # 그래서 l이 만약 r과 같거나 크다면 이 말인 즉슨, r을 키워야한다는 의미이다.
        while l >= r or (psum[r + 1] - psum[l - 1]) * 2 < total_dist:
            r += 1
            
        dist1 = min(psum[r] - psum[l - 1], total_dist - (psum[r] - psum[l - 1]))
        dist2 = min(total_dist - (psum[r + 1] - psum[l - 1]), (psum[r + 1] - psum[l - 1]))
        ans = max(ans, dist1, dist2)
        
    return ans


print(solution(n, dists))