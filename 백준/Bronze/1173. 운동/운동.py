N, m, M, T, R = map(int, input().split())

def solution(N, m, M, T, R):
    # 맥박 T만큼 상승 / 휴식 맥박 R만큼 감소
    # 맥박 최소 m / 맥박 최대 M
    # 운동을 N분하는데 필요한 시간
    # 초기 맥박 m
    X = m
    ex_t = 0
    total_time = 0
    while True:
        if ex_t == N:
            return total_time
        if X + T <= M:
            X += T
            ex_t += 1
        elif X == m:
            return -1
        else:
            X = max(X - R, m)
        total_time += 1
        # print(f"total: {total_time}, ex_t: {ex_t}, X: {X}")


print(solution(N, m, M, T, R))
