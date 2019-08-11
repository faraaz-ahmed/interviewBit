arr = list(map(int, input().split()))
start, stop = 0, 0
info = []
for i in range(0, len(arr)):
  if i > 0 and arr[i - 1] < 0 and arr[i] > 0:
    start = i
    stop = i
  elif arr[i] > 0 and i > 0:
    stop += 1
    # print([start, stop])
  if i > 0 and arr[i] < 0 and arr[i - 1] > 0:
    print([start, stop])
    info.append([start, stop])
  elif arr[i] < 0:
    continue
  if len(arr) == i + 1 and arr[i] > 0:
    info.append([start, stop])
    # stop = i + 1
print(max(info, key = lambda x : x[1] - x[0]), info)

filter



sum