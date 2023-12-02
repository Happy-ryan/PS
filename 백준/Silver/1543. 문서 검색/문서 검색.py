A = input()
B = input()

cnt = 0
s = 0
while s < len(A):
# for s in range(len(A)):
    e = s + len(B)
    subA = A[s:e]
    if subA == B:
        cnt += 1
        s += len(B)
    else:
        s += 1
print(cnt)