# your code goes here
def solution(a, b):
    if (a <= 2 and b <= 1) or (a <= 1 and b <= 2):
        print("Yes")
    else:
        print("No")
        
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    solution(a, b)