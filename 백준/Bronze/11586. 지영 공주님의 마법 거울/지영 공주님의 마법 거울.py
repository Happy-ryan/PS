N = int(input())
brr=[]
for _ in range(N) :
    arr= input()
    brr.append(arr)
K = int(input())
if K==1 :
    for i in range(N) :
        print(brr[i])
elif K==3 :
    for j in range(N) :
        print(brr[N-1-j])
else :
    for x in range(N) :
        new_list = list(brr[x])
        for y in range(N//2):
            new_list[y],new_list[N-1-y] = new_list[N-1-y],new_list[y]
        print("".join(new_list))

# 문자열 수정
# 문자열, 튜플 : immutable type 수정 불가 자료형
# 수정하기 위해서 첫 번째 방법 : 리스트 변환 후 문자열 재변환
# list()함수 사용해서 문자열 리스트화하기
# 수정 후 리스트를 문자열로 변환 > join함수 활용 > "".join(리스트)
# 수정하기 위해서 두 번째 방법 : replace 메소드 사용
# s = "hi hello"
# s.replace("h", "p")