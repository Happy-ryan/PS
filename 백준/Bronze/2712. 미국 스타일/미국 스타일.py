t = int(input())
for _ in range(t):
    n, s = input().split()
    if s == "kg":
        print(f"{float(n)*2.2046:.4f} lb")
    elif s == "lb":
        print(f"{float(n)*0.4536:.4f} kg")
    elif s == "l":
        print(f"{float(n)*0.2642:.4f} g")
    elif s == "g":
        print(f"{float(n)*3.7854:.4f} l")