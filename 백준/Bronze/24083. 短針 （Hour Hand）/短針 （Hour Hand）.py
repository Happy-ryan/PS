A = int(input())
B = int(input())
ans = (A + B) % 12
print(12 if ans == 0 else ans)