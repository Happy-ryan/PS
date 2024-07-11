t = int(input())

def solution(num: int):
    five = '++++ ' 
    one = '|'
    
    ans = ''
    
    ans += five * (num // 5)
    ans += one * (num % 5)
    
    return ans


for _ in range(t):
    num = int(input())
    print(solution(num))