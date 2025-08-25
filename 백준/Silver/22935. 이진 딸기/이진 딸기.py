t = int(input())

def solution(number):
    
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    # 29                            16

    
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 
    # 28                           15  

    
    dic = {
        0 : 0, 1: 1, 2 : 2, 3 : 3, 4 : 4, 5: 5,
        6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10,
        11: 11, 12 : 12, 13: 13, 14: 14,
        
        15: 13, 16 : 12, 17 : 11, 18: 10, 19 : 9, 20 : 8,
        21 : 7, 22 : 6, 23 : 5, 24 : 4, 25 : 3, 26 : 2, 27 : 1, 28 : 0}
    
    number = dic[(number - 1) % 28]
    number += 1
    
    # print("변형", number)
    
    def conv(n, m):
        if n == 0:
            return 0

        res = ''
        conv = '0123456789abcdef'
        while n:
            n, mod = divmod(n, m)
            res += conv[mod]
        
        return res[::-1]
    
    number = conv(number, 2)
    
    # print("변환", number)
    
    k = len(number)
    
    if k < 4:
        number = (4 - k) * '0' + number
        
    # print(number)
    
    ans = ''
    for x in number:
        if x == '0':
            ans += 'V'
        else:
            ans += '딸기'
    
    return ans
            

for _ in range(t):
    number = int(input())
    print(solution(number))