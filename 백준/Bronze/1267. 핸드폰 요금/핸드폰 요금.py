N = int(input())
second = list(map(int,input().split()))
Y_pay = 0
# 1.영식 요금제
# 0~29 10원// 30~59 20원// 60~89// 90~119 30원
for x in second:
    Y_pay += ((x //30)+1)*10

# 2. 민식 요금제
# 0~59 15원 // 60~119 30원// 120~179 45원
M_pay = 0
for y in second:
    M_pay += ((y//60)+1)*15

if Y_pay > M_pay: print('M',M_pay)
elif Y_pay < M_pay : print('Y', Y_pay)
else: print('Y','M',Y_pay)