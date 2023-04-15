t = int(input())
for _ in range(t):
    name, score = input().split()
    score = int(score)
    if score >= 97:
        print(f"{name} A+")
    elif score >= 90:
        print(f"{name} A")
    elif score >= 87:
        print(f"{name} B+")
    elif score >= 80:
        print(f"{name} B")
    elif score >= 77:
        print(f"{name} C+")
    elif score >= 70:
       print(f"{name} C")
    elif score >= 67:
       print(f"{name} D+")
    elif score >= 60:
       print(f"{name} D")
    else:
       print(f"{name} F")
       
    