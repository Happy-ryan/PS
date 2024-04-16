n = int(input())
tastes = list(map(int, input().split()))
k = int(input())


def solution(n, tastes, k):
    
    tmp = n
    cnt = 0
    while tmp > 1:
        tmp //= 2
        cnt += 1

    def divide(tastes, cover):
        result = []

        tmp_list = []
        for i in range(0, n, cover):
            row = []
            x = i
            for _ in range(cover):
                row.append(tastes[x])
                x += 1
            row.sort()
            tmp_list.append(row)

        for row in tmp_list:
            result.extend(row)

        return result

    for pow in range(1, cnt + 1):
        cover = 2**pow
        people_cnt = n // cover
        tastes = divide(tastes, cover)

        if people_cnt == k:
            # print(f"cover: {cover}, people_cnt: {n // cover}, 정답: {tastes}")
            return tastes
        # else:
        #     print(f"cover: {cover}, people_cnt: {n // cover}, tastes: {tastes}")


print(*solution(n, tastes, k))
