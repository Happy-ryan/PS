N = int(input())
q = []
arr = [ input().split() for _ in range(N)]
q_head = 0 # index를 의미한다.
for i in range(N):
    if arr[i][0] == "push":
        q.append(arr[i][1])
    elif arr[i][0] == "pop":
        if len(q) != q_head:
            print(q[q_head]) #q.pop(0) pop대신 head를 움직여서 pop의 효과 내기
            q_head += 1
        else : print(-1)
    elif arr[i][0] =="size": #q에서 길이는 = len(q)-head
        print(len(q)-q_head)
    elif arr[i][0]=="empty":
        if len(q) != q_head:
            print(0)
        else: print(1)
    elif arr[i][0]=="front":
        if len(q) != q_head:
            print(q[q_head]) # pop대신 head를 움직여서 인덱스이용해서 출력하기
        else : print(-1)
    elif arr[i][0]=="back":
        if len(q) != q_head:
            print(q[-1])
        else : print(-1)