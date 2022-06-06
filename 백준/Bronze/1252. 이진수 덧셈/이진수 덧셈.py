a, b = input().split()
def f(a):
    sum = 0
    for x in a:
        sum *= 2
        sum += int(x)
    return sum
c = f(a) + f(b)
ans = ''
if c == 0:
	ans = '0'
else :
	while c:
	    ans += str(c % 2)
	    c //= 2
print(ans[::-1])