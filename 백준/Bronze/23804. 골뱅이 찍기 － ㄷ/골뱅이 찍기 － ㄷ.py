# https://www.acmicpc.net/problem/23804
n = int(input())

for i in range(n):
    for j in range(n):
        print("@@@@@", end="")
    print()
    
for i in range(3 * n):
    for j in range(n):
        print("@", end="")
    print()

for i in range(n):
    for j in range(n):
        print("@@@@@", end="")
    print()