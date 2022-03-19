N = int(input())
score = list(map(float, input().split()))
max_score = max(score)
newsum = 0
for i in score :
    new_score = (i/max_score) * 100
    newsum += new_score
print(round(newsum/N, 2))

# 문제 포인트 : 리스트 입력 코드, for문 돌면서 리스트나 합 만들려면 미리 정의해놔야 for문 돌 때 삭제가 되지 않는다.
N = int(input())
score = list(map(float, input().split())) # 입력을 한 줄 리스트로 만드는 경우
max_score = max(score) 
newsum = 0 # 평균을 구하기 위해서 new_score의 합을 구해야하므로 미리 new_Sum 정의해놓기
for i in score :
    new_score = (i/max_score) * 100
    newsum += new_score # for문을 돌면서 new_sum에 값 저장시켜놓기
print(round(newsum/N, 2))
