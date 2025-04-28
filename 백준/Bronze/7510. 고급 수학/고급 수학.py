def solution(a, b, c):
    if (a ** 2 == b ** 2 + c ** 2) or\
        (b ** 2 == a **2 + c ** 2) or\
        (c ** 2 == a ** 2 + b ** 2):
            return True
    return False

t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    print(f"Scenario #{i + 1}:")
    if solution(a, b, c):
        print('yes')
    else:
        print('no')
    print()