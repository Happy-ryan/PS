G = int(input())

def solution(G):
    # G = 현재 몸무게의 제곱에서 성원이가 기억하고 있는 몸무게의 제곱을 뺌.
    # b^2 - a^2 = (b - a)(b + a)
    # G = b^2 - a^2
    # (G + a^2) ** 0.5 = 'b'
    
    ans = []
    a = 1
    for b in range(1, 100001):
        while a + 1 < b and (G + a ** 2) < b ** 2:
            a += 1
        
        if (G + a ** 2) ==  (b ** 2):
            ans.append(b)
    
    
    if not ans:
        ans.append(-1)
    
    for a in ans:
        print(a)
    
solution(G)