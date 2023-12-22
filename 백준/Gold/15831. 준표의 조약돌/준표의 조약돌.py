# https://www.acmicpc.net/problem/15831

n, b, w = map(int, input().split())
stones = [0] + list(input())

ans = 0
count_black_stone = 0
count_white_stone = 0


j = 0
for i in range(1, n + 1):
    # ex)검은돌이 1개가 최대일 때 1개가 되었을 때 while문 탈출하는 것을 고치지 못했음...ㅜㅠ
    # 그래서 <= 로 처리
    while j + 1 <= n and count_black_stone <= b:
        if stones[j + 1] == "B":
            count_black_stone += 1
        else:
            count_white_stone += 1
        j += 1

    # 검은 돌 b개 이하, 하얀 돌 w개 이상
    if count_black_stone <= b + 1 and count_white_stone >= w:
        if count_black_stone == b + 1:
            ans = max(ans, j - i)
        else:
            ans = max(ans, j - i + 1)

    # print(f"i: {i}, j: {j}, ans: {ans}, black: {count_black_stone}, white: {count_white_stone}")
    if stones[i] == "B":
        count_black_stone -= 1
    else:
        count_white_stone -= 1

print(ans)