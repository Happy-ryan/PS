# https://www.acmicpc.net/problem/9288
from itertools import combinations

def solution(num: int, case: int):
    print(f"Case {case}:")
    for x in range(1, 7):
        for y in range(1, 7):
            if x + y == num and x <= y:
                print(f"({x},{y})")
            
            
t = int(input())
for i in range(t):
    num = int(input())        
    solution(num, i + 1)