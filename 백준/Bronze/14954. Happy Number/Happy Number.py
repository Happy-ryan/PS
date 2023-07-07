def solution(n: int, level: int):
    if n // 10 == 0 and level != 0:
        if n == 1:
            return "Happy".upper()
        else:
            return "Unhappy".upper()

        
    if 1 <= n <= 9:
        return solution(n**2, level + 1)
    else:
        sum_val = 0
        for num in str(n):
            sum_val += int(num)**2
        return solution(sum_val, level + 1)
        
n = int(input())
print(solution(n, 0))