n = int(input(),8) #8진수 > 10진수 변환
# s = list(str(n))
# ten_num = 0
# for i in range(len(s)):
#     ten_num += int(s[i])*(8**(len(s)-1-i))
# print(ten_num)

# result = []
# while n != 1:
#     result.append(n%2)
#     n = n//2 
# result.append(1)
# result = result[::-1]
# # print(result)
# for i in result:
#     print(i,end='')
print(bin(n)[2:]) # 10진수 > 2진수 변환 내장함수 ob이진수 출력 [2:] 슬라이싱