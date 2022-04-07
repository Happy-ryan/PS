N = int(input())
arr = []
for _ in range(N) :
    num = int(input()) # N개의 숫자 입력
    arr.append(num) # 리스트에 담기
sort_list = sorted(arr) #리스트 안의 숫자들 정렬하기
for i in sort_list : # 정렬된 리스트에서 하나씩 포문 돌리면서 출력하면 한줄씩 완성
    print(i)