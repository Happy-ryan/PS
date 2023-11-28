i = 1

while True:
    n0 = int(input())

    if n0 == 0:
        break

    n1 = 3 * n0
    n2 = (n1 + 1) // 2 if n1 % 2 else n1 // 2
    n3 = 3 * n2
    n4 = n3 // 9

    result_type = "even" if n0 == 2 * n4 else "odd"

    print(f"{i}. {result_type} {n4}")
    i += 1
