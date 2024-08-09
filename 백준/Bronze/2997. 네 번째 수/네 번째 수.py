nums = list(map(int, input().split()))
nums.sort()

a, b, c = nums

d1 = b - a
d2 = c - b

# a y b c
# a b y c
# a b c y

if d1 == d2:
    print(c + d1)
else:
    y1 = a + d2
    y2 = b + d1

    if b - y1 == d2:
        print(y1)
    elif c - y2 == d1:
        print(y2)