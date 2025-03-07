A, B = map(int, input().split())
C, D = map(int, input().split())
answer = (A + B - 1) % 4
answer = (answer + C + D - 1) % 4
print(answer + 1)