n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]

# 고이지 않아야 한다!
# 높이가 증가 > 감소 > 증가 : 반드시 고인
# 고이지 않기 위해서는 증가 > 감소 | 증가만 | 감소만
# 증가만하는 경우는 왼쪽 -> see: 오른쪽을 바라보는
# 감소만하는 경우는 오른쪽 -> see: 왼쪽을 바라보는
# 양끝과 최대 높이 블록이 중요하다.
def solution(n, infos):
    # 정렬해도 큰 문제 없음!
    infos.sort(key=lambda x: x[0])
    s, init_high = infos[0]
    e, final_high = infos[-1]
    x_grid = []
    r_x_grid = []
    highs = []
    for x, h in infos:
        x_grid.append(x - s)
        r_x_grid.append(abs((e - s) - (x - s)))
        highs.append(h)

    k = e - s + 1

    max_high = max(highs)

    def see(highs, x_grid):
        x_stack = []
        high_stack = []
        for x in range(k):
            if len(x_stack) == 0:
                x_stack.append(x)
                high_stack.append(highs[x_grid.index(x)])
            else:
                x_stack.append(x)
                top_high = high_stack[-1]

                if x not in x_grid:
                    high_stack.append(top_high)
                else:
                    tmp_high = highs[x_grid.index(x)]
                    tmp_high = max(tmp_high, top_high)
                    high_stack.append(tmp_high)

        return high_stack

    total = []
    right = see(highs, x_grid)
    left = see(highs[::-1], r_x_grid[::-1])
    # print(right)
    # print(left)
    # print(right.index(max_high))
    # print(k - left.index(max_high))
    total.extend(right[:right.index(max_high) + 1])
    total.extend([max_high] * (k - left.index(max_high) - right.index(max_high) - 1))
    total.extend(left[:left.index(max_high)])
    # print(total)
    
    return sum(total)


print(solution(n, infos))
