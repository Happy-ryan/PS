a, b = map(int, input().split())

case1 = case2 = a * b

for x in range(1, a // 2 + 1):
    case1 = min(case1, a * b - 2 * b * x)
    # print(f"a * b - b * x : {a * b - b * x}. b * x : {b * x}")

for y in range(1, b // 2 + 1):
    case2 = min(case2, a * b - 2 * a * y)
    # print(f"a * b - a * y : {a * b - a * y}. a * y : {a * y}")
    
print(min(case1, case2))