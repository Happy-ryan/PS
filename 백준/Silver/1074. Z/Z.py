n, r, c = map(int, input().split())
# 정사각형이라서 같다.
W, H = 2 ** n, 2 ** n 
# tmp는 이동거리를 측정한다. W = 2가 되기 전까지 각 영역간 이동거리는 (W * W) // 4이다. 
# W = 2 가 되면 A(0), B(1), C(2), D(3)의 이동거리를 가진다.
tmp = 0
# 좌상단(A) / 우상단(B) / 좌하단(C) / 우하단(D)
# ans는 1/2 씩 축소하면서 어느 영역에 좌표가 존재하는지 확인한다.
ans = []

# r, c는 해당 영역의 top_lef_r, top_left_c 를 의미한다.
# W를 1/2 축소시키는 만큼 r, c도 좌표를 조정해야한다. <- point!
def find(W, r, c):
    global tmp
    if W == 1:
        # print(ans)
        print(tmp)
        return
    # 좌상단(A)
    if (0 <= r < W // 2) and (0 <= c < W // 2):
        if W == 2:  
            tmp += 0
        else:
            tmp += (W * W // 4) * 0
        ans.append('A')
        return find(W // 2, r, c)
    # 우상단(B)
    elif (0 <= r < W // 2) and (W // 2 <= c < W):
        if W == 2:  
            tmp += 1
        else:
            tmp += (W * W // 4) * 1 
        ans.append('B')
        return find(W // 2, r, c - W // 2)  
    # 좌하단(C) 
    elif (W // 2 <= r < W) and (0 <= c < W // 2):
        if W == 2:  
            tmp += 2
        else:
            tmp += (W * W // 4) * 2
        ans.append('C')
        return find(W // 2, r - W // 2, c)
    # 우하단(D)
    elif (W // 2 <= r < W) and (W // 2 <= c < W):
        if W == 2:  
            tmp += 3
        else:
            tmp += (W * W // 4) * 3
        ans.append('D')
        return find(W // 2, r - W // 2, c - W // 2)
    
find(W, r, c)