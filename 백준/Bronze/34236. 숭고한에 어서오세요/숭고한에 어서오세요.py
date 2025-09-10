n = int(input())
years = list(map(int, input().split()))
print(years[-1] + (years[-1] - years[-2]))