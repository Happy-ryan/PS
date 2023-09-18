# https://www.acmicpc.net/problem/2659
# 1111 ~ 9999 중에서 시계수를 찾기 > 브루트포스 가능

def is_clocknum(num: str):
    num1= num
    num2 = num1[1:] + num1[0]
    num3 = num2[1:] + num2[0] 
    num4 = num3[1:] + num3[0]
    res = min(num1,num2, num3, num4)
    return res

arr = set()
for num in range(1111, 10000):
    if '0' in str(num):
        continue
    arr.add(is_clocknum(str(num)))
arr = sorted(list(arr))

want = list(map(int, input().split()))
result = ''.join(map(str, want))
want_clock = is_clocknum(result)
print(arr.index(want_clock) + 1)