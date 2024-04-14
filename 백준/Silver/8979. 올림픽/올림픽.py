n, k = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(n)]


def solution(n, k, nations):
    nations.sort(key=lambda x: (-x[1], -x[2], -x[3]))

    arr = [1]
    for i in range(1, n):
        if nations[i][1:] == nations[i - 1][1:]:
            arr.append(arr[-1])
        else:
            arr.append(arr[-1] + 1)

    for idx, row in enumerate(nations):
        if row[0] == k:
            return arr[idx]


print(solution(n, k, nations))