n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


dic = {
    1: ("Yakk", "Habb Yakk"),
    2: ("Doh", "Dobara"),
    3: ("Seh", "Dousa"),
    4: ("Ghar", "Dorgy"),
    5: ("Bang", "Dabash"),
    6: ("Sheesh", "Dosh"),
}


def shout(a, b):
    if a == 5 and b == 6 or a == 6 and b == 5:
        return "Sheesh Beesh"
    if a == b:
        return dic[a][1]
    else:
        return dic[max(a, b)][0] + " " +dic[min(a, b)][0]


def solution(n, arr):
    for idx, row in enumerate(arr):
        a, b = row
        print(f"Case {idx + 1}: {shout(a, b)}")


solution(n, arr)