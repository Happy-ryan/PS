A, B = map(int,input().split())
a ="".join(reversed(str(A)))
b ="".join(reversed(str(B)))

result = max(a, b)

print(result)
