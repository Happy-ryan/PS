N, M = map(int, input().split())
T, S = map(int, input().split())

def solution(N, M, T, S):
    
    sleep_home = (N - 1) // 8
    time_home = N + sleep_home * S

    sleep_study = (M - 1) // 8
    time_study = M + sleep_study * (2 * T + S) + T

    if time_home < time_study:
        return "Zip", time_home
    else:
        return "Dok", time_study

res = solution(N, M, T, S)

print(res[0])
print(res[1])