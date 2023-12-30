def check(number: int) -> str:
    if number % 7 == 0 and number % 11 == 0:
        return "Wiwat!"
    if number % 7 == 0:
        return "Hurra!"
    if number % 11 == 0:
        return "Super!"
    return number
    
n = int(input())
for num in range(1, n + 1):
    print(check(num))