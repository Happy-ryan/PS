N = int(input())
arr=[input().split() for _ in range(N)]
result = []
for i in range(N) :
    if arr[i][0] == "push" : #리스트컴프리헨션때문에 행렬처럼 되었다. : 이차원의 배열처럼 되었다.
            result.append(arr[i][1]) # 스택은 후입선출 : 따라서 append추가하면 뒤에서부터 추가된다.
    elif arr[i][0] =="top" :
        if result==[] :
            print(-1)
        else : print(result[-1])
    elif arr[i][0] == "size" :
        print(len(result))
    elif arr[i][0] =="pop" :
        if result ==[] :
            print(-1)
        else : print(result.pop()) # pop() : arr[1,2,3] >> arr.pop() 3을 출력하고 arr=[1,2] 변경한다.
    elif arr[i][0] =="empty" :
        if result==[] :
            print(1)
        else : print(0)
