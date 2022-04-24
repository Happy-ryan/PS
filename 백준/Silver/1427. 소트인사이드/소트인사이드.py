N = int(input())
bucket =[ 0 for _ in range(10)]
for i in str(N) : 
    bucket[int(i)] += 1 # 0~9사이의 등장하는 정수의 갯수만 세면 되기 때문에 빈리스트 대신에 0으로 만들기
#print(bucket)
for i in range(10) :
    if bucket[9-i] == 0 : # 내림차순이므로 9부터 0으로 : 역순으로
        pass
    else :
        result = bucket[9-i]*str(9-i)
        print(result, end="")