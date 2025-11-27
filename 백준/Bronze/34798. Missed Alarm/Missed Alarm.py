ah, am = map(int, input().split(':'))
bh, bm = map(int, input().split(':'))

alarm = ah * 60 + am
now = bh * 60 + bm

print("YES" if now > alarm else "NO")