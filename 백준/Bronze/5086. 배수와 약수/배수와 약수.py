#https://www.acmicpc.net/problem/5086
# ~10000 : 시간초과 우려x

def f1(first, second):
    flag = False
    if second % first == 0:
        flag = True
    return flag


def f2(first, second):
    flag = False
    if first % second == 0:
        flag = True
    return flag


def solution(fisrt, second):
    if f1(fisrt, second):
        return "factor" 
    elif f2(fisrt, second):
        return "multiple"
    else:
        return "neither"
    
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(solution(a, b))