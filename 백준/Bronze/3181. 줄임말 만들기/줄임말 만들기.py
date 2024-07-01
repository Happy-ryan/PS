words = list(input().split())

exclude_word = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

ans = ''

for idx, word in enumerate(words):
    if word in exclude_word:
        if idx == 0:
            ans += word[0].upper()
    else:
        ans += word[0].upper()
        
print(ans)