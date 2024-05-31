while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    # 최대나이: 늦게 죽고 - 빨리 태어남
    max_age = d - a
    # 최소나이: 빨리 죽고 - 늦게 태어남
    min_age = c - b
    print(min_age, max_age)