k = int(input())

def solution(k):
    
    def conv(n, m):
        if n == 0:
            return 0
        res = ""
        conv = "0123456789abcdef"
        while n > 0:
            n, mod = divmod(n, m)
            res += conv[mod]
        return res[::-1]
            
    n = (2 ** k)  - 1
    sum_val = n * (n + 1) // 2
    
    
    return bin(sum_val)[2:]

print(solution(k))