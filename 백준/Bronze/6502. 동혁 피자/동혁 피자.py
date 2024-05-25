def solution(r, w, l):
    if 2 * r >= (w ** 2 + l ** 2) ** 0.5:
        return True
    return False

t = 1
while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1 and nums[0] == 0:
        break
    r, w, l = nums
    if r == 0:
        break
    if solution(r, l, w):
        print(f"Pizza {t} fits on the table.")
    else:
        print(f"Pizza {t} does not fit on the table.")
    t += 1