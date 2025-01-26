n = int(input())
m = int(input())

def solution(n, m):
    hands = [1, 2, 3, 4, 5, 4, 3, 2]
    
    
    if n == 1 or n == 5:
        cnt = m // 1
        check = cnt * 1
    else:
        cnt = m // 2
        check = cnt * 2
        
    num = cnt * 8
    
    # print(f"cnt: {cnt} / check: {check}")
    
    for hand in hands:
        if check == m + 1:
            break
        else:
            if hand == n:
                check += 1
            num += 1
        # print(f"hand: {hand} / num: {num}")
    
                
    return num - 1

        
print(solution(n, m))