# https://www.acmicpc.net/problem/4435/


def cal(arr, brr, idx):
    a1, a2, a3, a4, a5, a6 = arr
    b1, b2, b3, b4, b5, b6, b7 = brr

    sum_val1 = 1 * a1 + 2 * a2 + 3 * a3 + 3 * a4 + 4 * a5 + 10 * a6
    sum_val2 = 1 * b1 + 2 * b2 + 2 * b3 + 2 * b4 + 3 * b5 + 5 * b6 + 10 * b7

    if sum_val1 > sum_val2:
        return f"Battle {idx}: Good triumphs over Evil"
    elif sum_val1 < sum_val2:
        return f"Battle {idx}: Evil eradicates all trace of Good"
    else:
        return f"Battle {idx}: No victor on this battle field "


t = int(input())
for idx in range(1, t + 1):
    arr = map(int, input().split())
    brr = map(int, input().split())
    print(cal(arr, brr, idx))
