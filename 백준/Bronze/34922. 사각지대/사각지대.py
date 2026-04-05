from math import pi  

w, h = map(int, input().split())
r = int(input())

print(w * h - pi * r * r * (0.25))