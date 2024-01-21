# https://www.acmicpc.net/problem/10250
# 방 선호: 엘리베이터에서 가까운 순 > 같다면 낮은 층


def solution(H: int, W: int, N: int):
    # 1순위: 거리1 채우고 > 거리2 채우고.... 몇 호실?
    # H만큼 각 거리를 채우게 된다.
    XX = (N // H) + 1 if N % H != 0 else N // H
    # 2순위: 몇 층?
    YY = N % H if N % H != 0 else H
    return f"{YY}{XX:02}"
    

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    print(solution(H, W, N))