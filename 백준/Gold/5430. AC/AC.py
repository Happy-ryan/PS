# https://www.acmicpc.net/problem/5430
# --시간복잡도 계산
# R: 뒤집기 O(N)
# D: 첫 번째 원소 버리기 O(N)
# 최대 n = 100,000이므로 RD..몇 번만 시험하여도 시간복잡도 너무 커지게 됨
# -> O(100000*100 -> 10^6 * 10^2 * 10^2)

from collections import deque

def lis2ans(arr: list):
    ans = "["
    for x in arr[:-1]:
        ans += f"{x},"
    ans += str(arr[-1]) + "]"
    return ans


def solution(cmds: str, length: int, nums: list[int]):
    if cmds.count("D") > length:
        return "error"
    if cmds.count("D") == length:
        return "[]"

    nums = deque(nums)
    reverse_check = 0 # 0 정방향, 1 역방향
    for cmd in cmds:
        if cmd == "R":
            if reverse_check == 0:
                reverse_check = 1
            else:
                reverse_check = 0
        else:
            if reverse_check == 1:
                nums.pop()
            else:
                nums.popleft()

    if reverse_check == 1:
        return str(list(reversed(nums))).replace(" ", "")
    else:
        return  str(list(nums)).replace(" ", "")

t = int(input())
for _ in range(t):
    cmds = input()
    length = int(input())
    nums = eval(input())
    print(solution(cmds, length, nums))

