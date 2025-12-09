n = int(input())

for _ in range(n):
    name = input()
    if name == 'yonsei' or name == 'korea':
        print('Yonsei Won!' if name == 'yonsei' else 'Yonsei Lost...')
        break