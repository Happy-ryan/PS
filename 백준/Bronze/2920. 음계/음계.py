a, b, c, d, e, f, g, h = map(int, input().split())

if (a > b) and (b > c) and (c > d)and (d> e)and (e> f)and (f > g) and (g>h):
    print("descending")
elif (a < b) and (b < c) and (c < d)and (d <e)and (e < f)and (f < g) and (g<h):
    print("ascending")
else :
    print("mixed")