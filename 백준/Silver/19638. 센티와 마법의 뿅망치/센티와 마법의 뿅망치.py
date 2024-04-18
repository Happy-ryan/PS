n, h_centi, t = map(int, input().split())
heights = [int(input()) for _ in range(n)]

from heapq import heappush, heappop
import math

def solution(n, h_centi, t, heights):
    answer = ''
    # 센티의 키가 기준이 된다.

    # 전략: t번 가장 큰 거인을 내려친다.
    # 가장 큰 거인을 찾기 위해 max_heap을 사용한다.
    cnt = 0
    max_heap = []
    for height in heights:
        heappush(max_heap, -height)

    while True:
        max_height = -max_heap[0]
        # print(f"max_height: {max_height}")

        if max_height < h_centi:
            # print("YES")
            # print(cnt)
            answer = f"YES\n{cnt}"
            break

        if t == 0 or max_height == 1:
            # print("NO")
            # print(max_height)
            answer = f"NO\n{max_height}"
            break

        if max_height > 1:
            max_height = -heappop(max_heap)
            t -= 1
            cnt += 1
            heappush(max_heap, -math.floor(max_height / 2))

    return answer

print(solution(n, h_centi, t, heights))