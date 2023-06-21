# https://www.acmicpc.net/problem/2992
# 시간복잡도 계산: 1000000 > 자릿수의 관점 > 최대6자리 > 가능한 숫자의 최대 조합은 6!
# 따라서 O((log10(n))!)

# def list2num(arr:list[str]):
#     sum_val = 0
#     for idx, num in enumerate(arr):
#         sum_val += int(num) * 10**(len(arr) - idx - 1)
#     return sum_val


from functools import reduce
# --reduce: 리스트의 모든 값을 누적해 하나의 값으로 만들기 위해 사용
def list2num(arr: list[str]) -> int:
    return reduce(lambda x, y: x*10 + y, map(int, arr))

        
def solution(n: int):
    nums = list(str(n))
    # --
    used = [0] * len(nums)
    visited = []
    # --팩토리얼 구하는 방법
    def fact(level, depth):
        if level == depth and list2num(visited) > n:
            ret = list2num(visited)
            return ret
        ret = int(1e7)
        for i in range(len(nums)):
            if used[i] == 0:
                used[i] = 1
                visited.append(nums[i])
                ret = min(ret, fact(level + 1, depth))
                used[i] = 0
                visited.pop()
        return ret
    
    if fact(0, len(nums)) == int(1e7):
        return 0
    else:
        return fact(0, len(nums))


n = int(input())
print(solution(n))