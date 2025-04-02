n = int(input())
nums = list(map(int, input().split()))

from collections import deque


def solution(n, nums):
    q1 = deque([])
    q2 = deque([])

    for idx, num in enumerate(nums):
        if idx == 0:
            q1.append(idx + 1)
        else:
            if num == 0:
                q1.append(idx + 1)
            else:
                for _ in range(num):
                    q2.appendleft(q1.pop())
                q1.append(idx + 1)

                q1 += q2
                q2 = deque([])
        # print(f"{idx + 1} 학생 : {q1}, {q2}")
        
    return q1


print(*solution(n, nums))