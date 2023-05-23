t = int(input())
for _ in range(t):
    s = input()
    if "+" in s:
        a, b = s.split("+")
        print(int(a)+int(b))
    else:
        print("skipped")