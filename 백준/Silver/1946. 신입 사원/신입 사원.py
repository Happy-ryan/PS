T = int(input())

for _ in range(T):
    N = int(input())
    cnt = 1 # 마지막은 반드시 뽑힘.(면접 또는 서류가 1등이기 때문에)
    ranking = []
    x1_list = []
    for _ in range(N):
        a, b = map(int, input().split())
        ranking.append((a, b))
    # x[0]을 기준으로 정렬, x[1]만 비교하면 된다.
    # x[0] - 내림차순 정렬하여 이미 내 뒤로 나보다 서류 뛰어난 애들만 존재
    # x[1] - 면접 성적이 나보다 등수 낮은 애 있으면 난 무조건 탈락이다.
    ranking.sort( key = lambda x : x[0], reverse= True)
    
    for x0, x1 in ranking:
        x1_list.append(x1)
    # 나보다 인덱스 큰 놈 중에서 작은 값 있는지 확인하는 방법
    check = [x1_list[-1]]
    for i in reversed(range(N - 1)):
            check.append(min(check[-1], x1_list[i]))
    
    print(len(set(check)))
      