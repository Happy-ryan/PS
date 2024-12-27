n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cmds = [list(map(int, input().split())) for _ in range(k)]

from copy import deepcopy
from itertools import permutations

# combinations(iterable, r) : iterable에서 원소 개수가 r개인 조합 뽑기
# combinations_with_replacement(iterable,r) : iterable에서 원소 개수가 r개인 중복 조합 뽑기
# permutations(iterable,r=None) : iterable에서 원소 개수가 r개인 순열 뽑기
# product(*iterables, repeat=1) : 여러 iterable의 데카르트곱 리턴

def solution(n, m, k, board, cmds):
    inf = int(1e18)
    
    def A(board):
        val = inf
        for row in board:
            val = min(val, sum(row))
        return val 
    
    # '시계방향 회전' 하는 방법 익혀두기 - 시간복잡도 4 * size
    #  같은 껍데기레벨에 속하는 좌표들은 리스트 안에 넣는다. 그 이후에 그 리스트를 시계방향 회전시킨다!
    def get_group(l_r, l_c, size):
        # 상 -> 우 -> 하 -> 좌 순으로 모으기
        group = []
        for j in range(l_c, l_c + size):
            group.append((l_r, j))
        # group.append("/")
        for i in range(l_r + 1, l_r + size):
            group.append((i, l_c + size - 1))
        # group.append("/")
        for j in range(l_c + size -2, l_c - 1, -1):
            group.append((l_r + size - 1, j))
        # group.append("/")
        for i in range(l_r + size - 2, l_r, -1):
            group.append((i, l_c))
            
        return group
    
    # 시간복잡도 - 1
    def rotate_group(group):
    
        group = [group[-1]] + group[:-1]
    
        return group
    
    # 시간복잡도 - 
    def rotate(cmd):
        
        new_board = deepcopy(board)
        r, c, s = cmd
        
        l_r = r - s - 1
        l_c = c - s - 1
        size = 2 * s + 1

        while True:
            if size == 1:
                new_board[l_r][l_c] = board[l_r][l_c]
                break
            group = get_group(l_r, l_c, size) # 위치
            r_group = rotate_group(group) # 새로운 값
            
            # print(f"시작점: {l_r}, {l_c}")
            # print(f"group: {group} / 개수: {len(group)}")
            
            for grid, val in zip(group, r_group):
                new_board[grid[0]][grid[1]] = board[val[0]][val[1]]
            
            l_r += 1
            l_c += 1
            size -= 2
            
        
        # for row in new_board:
        #     print(*row)
            
        return new_board
            
    # 백트래킹이 사용되는 부분...연산 순서의 경우의 수에 대해서 최솟값을 찾아야하므로!
    # k가 6이므로 순서의 경우의 수는 6! = 720
    orgin_board = deepcopy(board)
    val = inf
    for row in permutations(cmds):
        for cmd in row:
            board = rotate(cmd)
        val = min(val, A(board))
        board = deepcopy(orgin_board) # board 원상복귀
    
    return val
    
    
print(solution(n, m, k, board, cmds))