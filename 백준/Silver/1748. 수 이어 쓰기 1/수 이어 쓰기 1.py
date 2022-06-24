n = int(input())
if n <10:
    print(n)
elif n < 100:
    print(9+2*(n-9))
elif n < 1000:
    print(189+3*(n-99))
elif n < 10000:
    print(2889+4*(n-999))
elif n < 100000:
    print(38889+5*(n-9999))
elif n < 1000000:
    print(488889+6*(n-99999))
elif n < 10000000:
    print(5888889+7*(n-999999))
elif n < 100000000:
    print(68888889+8*(n-9999999))
else:
    print(788888889+9*(n-99999999))