num = 0
while True:
    t = int(input())
    num += 1
    if t == 0:
        break
    dic = {}
    for i in range(1, t + 1):
        dic[i] = [input()]
    for _ in range(2 * t - 1):
        idx, check = input().split()
        dic[int(idx)].append(check)
    for key, value in dic.items():
        if len(value) != 3:
            print(f"{num} {value[0]}")