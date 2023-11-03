# https://www.acmicpc.net/problem/28290

def f(s):
    if s == "fdsajkl;" or s == "jkl;fdsa":
        return "in-out"
    if s == "asdf;lkj" or s == ";lkjasdf":
        return "out-in"
    if s == "asdfjkl;":
        return "stairs"
    if s == ";lkjfdsa":
        return "reverse"
    return "molu"
    
s = input()
print(f(s))
