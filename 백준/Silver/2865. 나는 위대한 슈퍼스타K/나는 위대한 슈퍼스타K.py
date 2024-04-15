n, m, k = map(int, input().split())
infos = []

for _ in range(m):
    genre = []
    row = list(input().split())
    for i in range(2 * n):
        if i % 2 == 0:
            genre.append(int(row[i]))
        else:
            genre.append(float(row[i]))
    infos.append(genre)


def solution(n, m, k, infos):

    all_case = []
    for genre, row in enumerate(infos):
        for i in range(0, len(row), 2):
            # 능력, 사람번호, 장르
            all_case.append((row[i + 1], row[i], genre))

    all_case.sort(key=lambda x: -x[0])

    # print(all_case)

    member = [0] * (n + 1)
    score = [0] * (n + 1)
    idx = 0
    while sum(member) < k:
        if member[all_case[idx][1]] == 0:
            member[all_case[idx][1]] = 1
            score[all_case[idx][1]] = all_case[idx][0]
        idx += 1

    # print(member)
    # print(score)
    return f"{sum(score):.1f}"


print(solution(n, m, k, infos))