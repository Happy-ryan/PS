N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

points = 0

for i in range(N):
    if A[i] > B[i]:
        points += 3
    elif A[i] == B[i]:
        points += 1

print(points)
