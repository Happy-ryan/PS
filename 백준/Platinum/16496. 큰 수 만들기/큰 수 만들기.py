from functools import cmp_to_key

N = int(input())
arr = list(map(int, input().split()))

def solution(numbers):
    def compare(x, y):
        if x == y: return 0
        xy = str(x) + str(y)
        yx = str(y) + str(x)
        if xy < yx:
            return 1
        else:
            return -1

    numbers.sort(key=cmp_to_key(compare))
    ans = ''
    for x in numbers:
        ans += str(x)
    if ans[0] == '0': ans = '0'
    return ans

print(solution(arr))