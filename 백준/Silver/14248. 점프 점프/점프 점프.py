n = int(input())
nums = list(map(int, input().split()))
s = int(input())

from collections import deque

def solution(n, nums, s):

    def bfs(s):
        visited = [False for _ in range(n)]
        cnt = 0

        def in_range(x):
            return 0 <= x < n

        dq = deque([])
        dq.append(s)
        visited[s] = True
        cnt += 1

        while dq:
            cx = dq.popleft()
            for k in [nums[cx], -nums[cx]]:
                nx = cx + k
                if in_range(nx) and not visited[nx]:
                    dq.append(nx)
                    visited[nx] = True
                    cnt += 1

        return cnt
    # 1base
    cnt = bfs(s - 1)

    return cnt


print(solution(n, nums, s))