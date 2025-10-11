D, C, R = map(int, input().split())
C_ = [int(input()) for _ in range(C)]
R_ = [int(input()) for _ in range(R)]

def solution(D, C, R, C_, R_):
    c_idx, r_idx = 0, 0
    cnt = 0

    # 둘 다 남아있는 동안 규칙대로 진행
    while c_idx < C and r_idx < R:
        if D >= C_[c_idx]:
            D -= C_[c_idx]
            c_idx += 1
        else:
            D += R_[r_idx]
            r_idx += 1
        cnt += 1

    # 만약 모든 피로 활동을 이미 끝냈다면 남은 활력 활동은 전부 수행 가능
    if c_idx == C:
        cnt += (R - r_idx)
        return cnt

    # 만약 활력 활동이 바닥났다면, 남은 피로 활동들 중 수행 가능한 것들만 계속 수행
    while c_idx < C and D >= C_[c_idx]:
        D -= C_[c_idx]
        c_idx += 1
        cnt += 1

    return cnt

print(solution(D, C, R, C_, R_))