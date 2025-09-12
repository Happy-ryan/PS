n = int(input())
b1 = input()
b2 = input()

def solution(n, b1, b2):
    
    def change(x):
        b = ''
        for x in b1:
            if x == '1':
                b += '0'
            else:
                b += '1'
        return b
    
    for _ in range(n):
        b = change(b1)
        b1 = b
        
    if b1 == b2:
        return 'Deletion succeeded'

    return 'Deletion failed'


print(solution(n, b1, b2))