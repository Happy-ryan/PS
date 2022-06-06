a,b = map(int, input().split())

def f(x) : #이진수x를 십진수로 변환하는 함수
    sum = 0
    for i in range(len(str(x))):
        sum += int(str(x)[i])*(2**(len(str(x))-1-i))
    return sum
result = str(f(a)+f(b)) #type int
if result =='0':
    print(0)
else:
  ans = ''
  result = int(result)
  while result:
      ans += str(result % 2)
      result //= 2
  print(ans[::-1])