n = int(input(),2) # 2진수 > 10진수 변환
# print(n)
result = []
while n >= 8:
    result.append(n%8)
    n = n//8 
result.append(n)
# print(result)
for i in result[::-1]:
    print(i,end="")