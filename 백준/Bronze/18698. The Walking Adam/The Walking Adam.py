t = int(input())
for _ in range(t):
    s = input()
    if "D" in s:
        s = s.split("D")[0]
    print(s.count("U"))