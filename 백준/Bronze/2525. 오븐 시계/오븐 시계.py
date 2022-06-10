A, B = map(int, input().split()) # A = 시, B = 분
C = int(input())
# 0시0분에서 더한다고 생각하자, minute = (A * 60 + B + C) % (24 * 60)
# print(minute // 60, minute % 60)

B += C
A += B // 60
B = B%60
A = A%24
print(A, B)