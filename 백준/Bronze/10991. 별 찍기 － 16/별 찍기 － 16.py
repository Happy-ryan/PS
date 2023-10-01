#   * - 3 + (1 + 빈)
#  * * - 2 + (1 + 빈) + (1 + 빈)
# * * * - 1 + (1 + 빈) + (1 + 빈) + (1 + 빈)
#* * * * - 0 + (1 + 빈) + (1 + 빈) + (1 + 빈) + (1 + 빈)

n = int(input())

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end=" ")
    print()