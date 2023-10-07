from math import pi

a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())
a2 = r1**2*pi

if p1/a1 < p2/a2:
    print("Slice of pizza")
else:
    print("Whole pizza")