c1 = input()
c2 = input()

x, y = abs(ord(c1[0]) - ord(c2[0])), abs(int(c1[1]) - int(c2[1]))

val_x = min(x, y)
val_y = max(x, y)

print(val_x, val_y)