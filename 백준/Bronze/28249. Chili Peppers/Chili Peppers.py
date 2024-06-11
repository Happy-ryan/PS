n = int(input())
menus = [input() for _ in range(n)]

def solution(menus):
    menu_price = {'Poblano': 1500,
                    'Mirasol': 6000,
                    'Serrano': 15500,
                    'Cayenne': 40000,
                    'Thai': 75000,
                    'Habanero': 125000}
    
    ans = 0
    for menu in menus:
        ans += menu_price[menu]
        
    return ans

print(solution(menus))