dex = list(map(int, input().split()))
print(dex)
current_sum, max_sum_so_far = 0, 0
start, s, end = 0, 0, 0
for i in range(len(dex)):
  current_sum += dex[i]
  if current_sum < 0:
    current_sum = 0
    s = i + 1
  elif current_sum >= max_sum_so_far:
    max_sum_so_far = current_sum
    start = s
    end = i
    # s = i + 1
    print([start, end])

print(start, end)

