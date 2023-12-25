a, b, c, d, N = map(int, input().split())

sum_val = a + b + c + d
total_sum_val = 4 * N

need = total_sum_val - sum_val

print(need if need > 0 else 0)