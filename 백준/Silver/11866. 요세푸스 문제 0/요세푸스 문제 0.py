# https://www.acmicpc.net/problem/11866

from collections import deque

n, k = map(int, input().split())
q = deque(list(range(1, n + 1)))

ans = []
while q:
    for _ in range(k - 1):
        # 1번째 ~ k - 1번째 사람은 원은 순환해야함.
        # popleft로 빼고 append로 다시 맨 뒤로 넣음
        q.append(q.popleft())
    # k번째 일 때는 다시 넣지 않고 popleft만 시킨다.
    ans.append(q.popleft())
    
def makePrintFormat(nums: int):
    ans = ""
    for x in nums[:-1]:
        ans += str(x)+", "
    ans += str(nums[-1])
    return "<" + ans + ">"

print(makePrintFormat(ans))