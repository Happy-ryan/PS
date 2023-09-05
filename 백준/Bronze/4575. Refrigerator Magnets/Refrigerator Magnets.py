from collections import Counter

while True:
    s = input()
    if s == "END":
        break
    dic = Counter(s)
    flag = True
    for key, value in dic.items():
        if key != ' ' and value > 1:
            flag = False
            break
    if flag:
        print(s)