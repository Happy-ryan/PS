S = input()

def solution(S):
    
    dic = {
        'A':3,'B':2,'C':1,'D':2,'E':3,'F':3,'G':3,'H':3,
        'I':1,'J':1,'K':3,'L':1,'M':3,'N':3,'O':1,'P':2,
        'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':2,'X':2,
        'Y':2,'Z':1
    }

    arr = [dic[c] for c in S]
    
    # 숫자가 하나 남을 때까지 반복
    while len(arr) > 1:
        next_arr = []
        i = 0
        
        while i + 1 < len(arr):
            next_arr.append((arr[i] + arr[i+1]) % 10)
            i += 2
        
        # 홀수 개면 마지막 하나 그대로
        if i < len(arr):
            next_arr.append(arr[i])
        
        arr = next_arr
    
    # 마지막 수의 홀짝
    return "I'm a winner!" if arr[0] % 2 == 1 else "You're the winner?"

print(solution(S))