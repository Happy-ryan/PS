n = int(input())
arr = [ input().split() for _ in range(n)]
# print(arr)
def anagram(row):
    s1 = sorted(list(row[0]))
    s2 = sorted(list(row[1]))
    if s1==s2:
        return "{0} & {1} are anagrams.".format(row[0],row[1])
    else:
        return "{0} & {1} are NOT anagrams.".format(row[0],row[1])

for row in arr:
    print(anagram(row))