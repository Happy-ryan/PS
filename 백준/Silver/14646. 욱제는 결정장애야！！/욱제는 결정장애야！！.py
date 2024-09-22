n = int(input())
menus = list(map(int, input().split()))

def solution(n, menus):
    stickers = [0] * (n + 1)
    sum_val = 0
    delete_menu = set()
    max_stickers = 0
    # 0. 돌림판을 돌림
    for menu in menus:
        # 1. 스티커가 없으면 붙임
        if stickers[menu] == 0:
            stickers[menu] = 1
            sum_val += 1
        # 2. 스티커가 있다면 메뉴 적고 돌림판칸에서 제거.
        else:
            # 2-1. 돌림판 제거 안 된 상태
            if menu not in delete_menu:
                delete_menu.add(menu)
                stickers[menu] = 0
                sum_val -= 1
        # 최대 스티커 갱신
        max_stickers = max(max_stickers, sum_val)
    
    return max_stickers

print(solution(n, menus))