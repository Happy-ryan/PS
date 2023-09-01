def hanoi(n, s, e):
    if n == 1:
        print(s, e)
        return
    hanoi(n - 1, s, 6 - s - e)
    print(s, e)
    hanoi(n - 1, 6 - s - e, e)

n = int(input())
# 하노이탑 퍼즐의 최소 이동 회수: 2^n - 1
# Python에서는 2**n 사용 가능
print(2**n - 1)
hanoi(n, 1, 3)