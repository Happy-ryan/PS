n = int(input())

def reverseNum(x: str) -> int:
    return int(x[::-1])

for _ in range(n):
    a, b = input().split()
    a, b = reverseNum(a), reverseNum(b)
    res = reverseNum(str(a + b))
    print(res)