n = int(input())

arr = [input() for _ in range(n)]

def solution(arr):
    
    for x in arr:
        answer = ''
        for i in range(len(x) - 1, -1, -1):
            answer += x[i]
        print(answer)
        
solution(arr)