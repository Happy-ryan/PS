# https://www.acmicpc.net/problem/21758

from copy import deepcopy

n = int(input())
honeys = list(map(int, input().split()))

# case1) 꿀통이 양 끝에 존재하는 경우
# 양 끝에 존재하면 벌통 1개의 위치는 꿀통이 존재하는 곳의 정확히 반대에 존재한다.
# 왜냐하면 꿀통으로부터 가장 멀리 떨어져 있어야 가장 많이 먹을 수 있기 때문에
# 따라서 나머지 1개는 양끝을 제외한 어딘가에 존재하게 된다. -> 시간복잡도 O(N)

# case2) 꿀통이 양 끝에 존재하지 않는 경우
# 꿀통이 양 끝에 존재하지 않는다면 벌들이 양끝에 존재해야한다.
# 왜냐하면 case1)를 생각하면 된다.
# 그런데 꿀통의 왼쪽 또는 오른쪽에 벌통이 몰려 있는 경우도 있지 않느냐?
# 그건 최대값이 될 수 없다.
# 꿀통의 왼쪽에 몰려있다고 했을 때 만약 꿀통의 오른쪽에 10억꿀이 있으면 최대가 아니다.
# 오른쪽도 마찬가지이다.
# 따라서 꿀통이 양끝에 존재하지 않는 경우(O(n))에는 벌통은 반드시 양끝에 존재했을 때
# 최대 꿀을 얻게 된다.


def solution(n, honeys):
    # case1) 꿀통이 양쪽에 존재하는 경우
    # case 1-1) 왼쪽 끝에 꿀통이 존재 <-> 오른쪽 끝에 벌통 존재
    # psum의 정의: 왼쪽 꿀통에서 벌통 위치까지 꿀의 누적합
    psum_left = [0] * (n + 1)
    for i in range(n):
        psum_left[i + 1] = psum_left[i] + honeys[i]

    max_val_left = -int(1e18)
    # 오른쪽 끝에 있는 벌통이 먹는 꿀의 양
    init_val_left = psum_left[n] - honeys[n - 1]
    for i in range(n - 1, 1, -1):
        # 가운데 벌통이 생기면 init_val_left에서 새롭게 선정한 벌통이 더해진 만큼은 제외한다.
        max_val_left = max(
            max_val_left, init_val_left - honeys[i - 1] + psum_left[i] - honeys[i - 1]
        )

    # print("left", max_val_left)

    # case1) 꿀통이 양쪽에 존재하는 경우
    # case 1-2) 오른쪽끝에 꿀통이 존재 <-> 왼쪽 끝에 벌통 존재
    # psum_right의 정의: 오른쪽 꿀통에서 벌통 위치까지 꿀의 누적합
    # honeys 뒤집기
    reversed_honey = deepcopy(honeys)[::-1]
    psum_right = [0] * (n + 1)
    for i in range(n):
        psum_right[i + 1] = psum_right[i] + reversed_honey[i]

    max_val_right = -int(1e18)
    # 오른쪽 끝에 있는 벌통이 먹는 꿀의 양
    init_val_right = psum_right[n] - reversed_honey[n - 1]
    for i in range(n - 1, 1, -1):
        # 가운데 벌통이 생기면 init_val_right에서 새롭게 선정한 벌통이 더해진 만큼은 제외한다.
        max_val_right = max(
            max_val_right,
            init_val_right
            - reversed_honey[i - 1]
            + psum_right[i]
            - reversed_honey[i - 1],
        )
        
        # print("right", max_val_right)

    # 꿀통이 가운데 있는 경우 & 벌통은 양쪽에 있음
    max_val_middle = -int(1e18)
    for i in range(1, n - 1):
        # 오른쪽 끝 벌통
        sum_val_right = psum_left[n] - psum_left[i] - honeys[n - 1]
        # 왼쪽 끝 벌통
        sum_val_left = psum_left[i + 1] - honeys[0]
        
        max_val_middle = max(max_val_middle, sum_val_left + sum_val_right)

    # print("middle", max_val_middle)
    
    return max(max_val_left, max_val_middle, max_val_right)

print(solution(n, honeys))