n = int(input())
sum = 0
zero_num = 0
for x in str(n):
    sum += int(x)
    if int(x) == 0:
        zero_num +=1
# print(sum)
# print(zero_num)
# 30의 배수 = 3의배수 * 10의배수 형태 = xxxxx0꼴 xxxx만으로 이미 3의배수
if sum%3 != 0 or zero_num == 0:
    print(-1)
else:
    num_list = sorted(list(str(n)))[::-1]
    print(*num_list,sep='')