n, a, b = map(int, input().split())
s, t = map(int, input().split())

if a < s < b and a < t < b:
    print("City")
elif s <= a and t <= a or s >= b and t >= b:
    print("Outside")
else:
    print("Full")