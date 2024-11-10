n = int(input())
s = input()

dic = {'v': ('q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v')}

if s[-1] in dic['v']:
    print(1)
else:
    print(0)