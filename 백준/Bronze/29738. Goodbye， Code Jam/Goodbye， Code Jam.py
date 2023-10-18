def check_round(num: int):
    if num <= 25:
        return "World Finals"
    if num <= 1000:
        return "Round 3"
    if num <= 4500:
        return "Round 2"
    return "Round 1"

t = int(input())
for i in range(1, t + 1):
    num = int(input())
    print(f"Case #{i}: {check_round(num)}")