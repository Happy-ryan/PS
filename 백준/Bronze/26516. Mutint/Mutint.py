def solution(M):

    def find_max(x):
        idx = len(str(x)) - 1
        num = 0
        res = []
        while x > 0:
            res.append((x % 10, idx))
            idx -= 1
            x //= 10

        res.sort(key=lambda x: (-x[0], x[1]))
        return res[0]

    num, idx = find_max(M)

    if num % 2 == 0:
        num += 4
        if num > 9:
            num %= 10
    else:
        num = 0

    res = str(M)[:idx] + str(num) + str(M)[idx + 1 :]

    return int(res)


while True:
    M = int(input())
    if M == 0:
        break
    print(solution(M))