# https://www.acmicpc.net/problem/11441

def solution(arr: list, test: list[list[int, int]]) -> int:
    psum = [0] * (len(arr) + 1)
    
    for i in range(len(arr)):
        psum[i + 1] = psum[i] + arr[i]
        
    # return psum
        
    for row in test:
        s, e = row
        if s == e:
            print(arr[e - 1])
        else:
            print(psum[e] - psum[s - 1])
            
        
n = int(input())
arr = list(map(int, input().split()))
t = int(input())
test = [list(map(int, input().split())) for _ in range(t)]

solution(arr, test)