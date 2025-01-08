a = int(input())
b = int(input())
c = int(input())
val1, val2, val3  = a + b, a + c, b + c

if val1 == c or val2 == b or val3 == a:
    print(1)
else:
    print(0)