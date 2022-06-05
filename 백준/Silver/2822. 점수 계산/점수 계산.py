arr = [int(input()) for _ in range(8)]
brr = sorted(arr)[::-1]
print(sum(brr[0:5]))
score = {}
for i in range(1,9):
  score[i] = arr[i-1] # dict에서 추가하는 방법
# print(score)
reverse_score = dict(map(reversed,score.items()))
# print(reverse_score)

reverse_score = sorted(list(reverse_score.items())) # items 써서 tuple로 변환 후 list 만들고 sorted하기
# print(reverse_score[0])
# print(reverse_score[1])
# print(reverse_score[2])
# print(reverse_score[3])
# print(reverse_score[4])
# print(reverse_score[5])
# print(reverse_score[6])
# print(reverse_score[7])
result = []
for i in range(3,8):
  result.append(reverse_score[i][1])
print(*sorted(result))