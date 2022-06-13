N = int(input())
sum1 = 0 # 학점시수시간 * 학점 
sum2 = 0 # 학점시수시간 총합
for _ in range(N): 
  arr = input().split()
  score = arr[2] 
  if score =='A+':
    score_num = 4.3
  elif score=="A0":
    score_num = 4.0
  elif score=="A-":
    score_num = 3.7
  elif score=="B+":
    score_num = 3.3
  elif score=="B0":
    score_num = 3.0
  elif score=="B-":
    score_num = 2.7
  elif score=="C+":
    score_num = 2.3
  elif score=="C0":
    score_num = 2.0
  elif score=="C-":
    score_num = 1.7
  elif score=="D+":
    score_num = 1.3
  elif score=="D0":
    score_num = 1.0
  elif score=="D-":
    score_num = 0.7
  else: score_num = 0.0
  sum1 += int(arr[1])*score_num
  sum2 += int(arr[1])
# print(sum1)
# print(sum2)
result = sum1 / sum2
# print(result)
result = result+0.00000000001 
print('{:.2f}'.format(result)) # format이용해서 소수점 자리 나타내기