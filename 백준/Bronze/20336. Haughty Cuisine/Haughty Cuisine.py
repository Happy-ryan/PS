n = int(input())
sets = [input().split() for _ in range(n)]

print(sets[0][0])
for menu in sets[0][1:]:
    print(menu)