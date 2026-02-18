R, C = map(int, input().split())
A, B = map(int, input().split())

def solution(R, C, A, B):
    
    p1 = [['.' for _ in range(C * B)] for _ in range(A)]
    p2 = [['.' for _ in range(C * B)] for _ in range(A)]
    
    for r in range(0, A):
        for c in range(0, C * B, 2 * B):
            for j in range(c, c + B):
                p1[r][j] = 'X'
                
    for r in range(0, A):
        for c in range(B, C * B, 2 * B):
            for j in range(c, c + B):
                p2[r][j] = 'X'
                
    for r1 in range(0, R):
        if r1 % 2 == 0:
            for row in p1:
                print(''.join(row))
        else:
            for row in p2:
                print(''.join(row))
    
solution(R, C, A, B)