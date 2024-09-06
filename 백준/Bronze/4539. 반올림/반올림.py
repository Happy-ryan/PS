# https://www.acmicpc.net/problem/4539
n = int(input())

def custom_round(num:int):
    if num <= 10:
        return num
    
    mod = 10
    while True:
        if mod >= num:
            return num
        # mod 단위
        part1 = num // mod
        # mod 바로 아래 단위
        part2 = ( num % mod ) // ( mod // 10 )
        if part2 < 5:
            part2 = 0
        else:
            part2 = mod
        
        num = part1 * mod + part2 
        # print(f"mod: {mod}, num: {num}")
        mod *= 10
        
for _ in range(n):
    t = int(input())
    print(custom_round(t))