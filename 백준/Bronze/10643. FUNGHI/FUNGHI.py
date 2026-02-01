s = [int(input()) for _ in range(8)]

s2 = s + s

max_mushrooms = 0
for i in range(8):
    max_mushrooms = max(max_mushrooms, sum(s2[i:i+4]))

print(max_mushrooms)