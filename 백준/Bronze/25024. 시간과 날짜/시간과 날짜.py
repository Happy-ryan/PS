def is_time(x, y):
    if 0 <= x <= 23 and 0 <= y <= 59:
        return 'Yes'
    return 'No'

def is_day(x, y):
    if x  in [1, 3, 5, 7, 8, 10, 12] and 1 <= y <= 31:
        return 'Yes'
    if x in [4, 6, 9, 11] and 1 <= y <= 30:
        return 'Yes'
    if x in [2]  and 1 <= y <= 29:
        return 'Yes'
    return 'No'

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(is_time(x, y), is_day(x, y))