a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())
res1 = a + max(T - 30, 0) * x * 21
res2 = b + max(T - 45, 0) * y * 21
print(res1, res2)