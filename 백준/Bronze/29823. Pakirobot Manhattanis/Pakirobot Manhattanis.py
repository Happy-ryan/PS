N = int(input())
arr = list(input())

x = abs(arr.count('E') - arr.count('W'))
y = abs(arr.count('N') - arr.count('S'))

ans = x + y

print(ans)