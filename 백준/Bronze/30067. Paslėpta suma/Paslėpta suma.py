total_number = [int(input()) for _ in range(10)]

total_sum = sum(total_number)

for num in total_number:
    if num == total_sum - num:
        print(num)
        break