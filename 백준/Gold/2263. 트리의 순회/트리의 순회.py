import sys
sys.setrecursionlimit(10**5)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

def solution(n, in_order, post_order):
    pre_order = []

    in_order_dict = {}
    for i, x in enumerate(in_order):
        in_order_dict[x] = i
       
    
    def find_pre_order(in_l, in_r, post_l, post_r): # [in_l, in_r), [post_l, post_r)
        if in_l == in_r:
            return
        root = post_order[post_r-1]

        # root_index = in_order.index(root) # 시간복잡도: O(n)
        # left_in_order = in_order[:root_index]
        # right_in_order = in_order[root_index+1:]
        # left_post_order = post_order[:len(left_in_order)]
        # right_post_order = post_order[len(left_in_order):-1] # root 제외

        root_index = in_order_dict[root] # 시간복잡도: O(1)
        left_size = root_index - in_l

        pre_order.append(root)
        find_pre_order(in_l, root_index, post_l, post_l + left_size)
        find_pre_order(root_index + 1, in_r, post_l + left_size, post_r - 1)
    
    find_pre_order(0, n, 0, n)

    return pre_order

print(*solution(n, in_order, post_order))