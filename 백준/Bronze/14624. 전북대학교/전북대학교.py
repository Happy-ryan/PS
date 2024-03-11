n = int(input())
if n % 2 == 0:
    print("I LOVE CBNU")
else:
    print("*" * n)
    k = n // 2 + 1
    for i in range(k):
        if i == 0:
            print(" " * (n // 2 - i) + "*")
        else:
            print(" " * (n // 2 - i) + "*" + " " * (i * 2 - 1) + "*")