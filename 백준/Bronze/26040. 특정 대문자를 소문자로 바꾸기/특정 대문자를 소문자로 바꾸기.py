s = input()
arr = list(input())
for x in arr:
    s = s.replace(x, x.lower())

print(s)