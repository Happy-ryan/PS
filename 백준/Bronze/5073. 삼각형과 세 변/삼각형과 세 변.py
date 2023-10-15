# https://www.acmicpc.net/problem/5073

def is_triangle(a, b, c):
    if a + b <= c:
        return "Invalid"
    elif a == b and b == c and a == c:
        return "Equilateral"
    elif a != b and b != c and c != a:
        return "Scalene"
    else:
        return "Isosceles"
    
while True:
    a, b, c = sorted(list(map(int, input().split())))
    if a == 0 and b == 0 and c == 0:
        break
    print(is_triangle(a, b, c))