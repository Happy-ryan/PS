# https://www.acmicpc.net/problem/29790
N, U, L = map(int, input().split())


def f(N, U, L):
    if N>=1000 and (U>=8000 or L>=260):
        return "Very Good"
    if N>=1000:
        return "Good"
    else:
        return "Bad"
    
print(f(N,U,L))