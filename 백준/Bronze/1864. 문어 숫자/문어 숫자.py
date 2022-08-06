decode ={"-":0,
        "\\": 1,
        "(": 2,
        "@": 3,
        "?": 4,
        ">": 5,
        "&": 6,
        "%": 7,
        "/":-1}

def f(s):
    sum = 0
    for i in range(len(s)):
        sum += decode[s[i]]*(8**(len(s)-i-1))
    return sum


while True:
    s = input()
    if s=="#":
        break
    else:
        print(f(s))