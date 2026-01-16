while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1:
        break
    N, P = nums[0], nums[1]
    # N은 무조건 4의 배수
    pages = [[] for _ in range((N // 4) + 1)]
    
    ps = list(range(1, N + 1))
    
    # 1 2 3 4 5 6 7 8 9 10 11 12
    pn = 1
    check_pn = 0

    for idx in range(0, N // 2, 2):
        pages[pn].append(ps[idx])
        pages[pn].append(ps[idx  + 1])
        pages[pn].append(ps[N - idx - 1])
        pages[pn].append(ps[N - idx - 2])
        

        if P in pages[pn]:
            check_pn = pn
            
        pn += 1
        
        
    answer = []
    pages[check_pn].sort()
    for p in pages[check_pn]:
        if p != P:
            print(p, end = ' ')