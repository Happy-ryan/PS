def make_psum_2D(board):
    psum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for r in range(n):
        for c in range(n):
            psum[r + 1][c + 1] = board[r][c] + psum[r + 1][c] + psum[r][c+ 1] - psum[r][c]
            
    return psum

def cal(top_r, top_c, bottom_r, bottom_c):
    return psum[bottom_r + 1][bottom_c + 1] - psum[bottom_r + 1][top_c] - psum[top_r][bottom_c + 1] + psum[top_r][top_c]
    
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
psum = make_psum_2D(board)

cnt = 0
for sr in range(0, n - 1):
    for sc in range(0, n - 1):
        # print(f"공유 꼭지점 - r: {sr}, c: {sc}")
        ans1 = []
        ans2 = []
        ans3 = []
        ans4 = []
        for r in range(0, sr + 1):
            for c in range(0, sc + 1):
                # print(f"왼쪽 상단 - x: {sr}, y: {sc}, r: {r}, c: {c}")
                ans1.append(cal(r, c, sr, sc))
        for r in range(sr + 1, n):
            for c in range(sc + 1, n):
                # print(f"오른쪽 하단 - x: {sr}, y: {sc}, r: {r}, c: {c}")
                k2 = cal(sr + 1, sc + 1, r, c)
                cnt += ans1.count(k2)
                ans2.append(cal(sr + 1, sc + 1, r, c))
        # print(ans1)
        # print(ans2)
        
        # print("=")
        for r in range(0, sr + 1):
            for c in range(sc + 1, n):
                # print(f"오른쪽 상단 - x: {sr}, y: {sc}, r: {r}, c: {c}")
                ans3.append(cal(r, sc + 1, sr, c))
        for r in range(sr + 1, n):
            for c in range(0, sc + 1):
                # print(f"왼쪽 하단 - x: {sr}, y: {sc}, r: {r}, c: {c}")
                k4 = cal(sr + 1, c, r, sc)
                cnt += ans3.count(k4)
                ans4.append(cal(sr + 1, c, r, sc))
        # print(ans3)
        # print(ans4)
        # print(f"cnt: {cnt}")
        # print("++++++++")
                
print(cnt)