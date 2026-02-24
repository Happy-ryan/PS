n = int(input())
s = input()

word1 = 'security'
word2 = 'bigdata'

cnt1, cnt2 = 0, 0

idx = 0
while idx < len(s):
    if s[idx] == 's':
        cnt1 += 1
        idx += len(word1)
    else:
        cnt2 += 1
        idx += len(word2)
        
if cnt1 > cnt2:
    print('security!')
elif cnt1 < cnt2:
    print('bigdata?')
else:
    print('bigdata? security!')