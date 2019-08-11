def generateMatrix(A):
  n = A * A
  arr = []
  for i in range(A):
      arr.append([])
      for j in range(A):
          arr[i].append(0)
  count = 1
  direction = "right"
  i = 0
  j = 0
  while(count <= n):
      if direction == "right" and j < A - 1:
          if arr[i][j] == 0:
              arr[i][j] = count
              # print("right", count)
              count += 1
              j = j + 1
              if j == A - 1 or not arr[i][j + 1] == 0:
                  direction = "down"
          else:
              j = j - 1
              direction = "down"
      elif direction == "left" and j > 0:
          if arr[i][j] == 0:
              arr[i][j] = count
              # print("left", count)
              count += 1
              j = j - 1
              if j == 0 or not arr[i][j - 1] == 0:
                  direction = "up"
          else:
              j = j + 1
              direction = "up"
      elif direction == "up" and i > 0:
          if arr[i][j] == 0:
              arr[i][j] = count
              # print("up", count)
              count += 1
              i = i - 1
              if i == 0 or not arr[i - 1][j] == 0:
                  direction = "right"
          else:
              i = i + 1
              direction = "right"
      elif direction == "down" and i < A - 1:
          if arr[i][j] == 0:
              arr[i][j] = count
              # print("down", count)
              count += 1
              i = i + 1
              if i == A - 1 or not arr[i + 1][j] == 0:
                  direction = "left"
          else:
              i = i - 1
              direction = "left"
      elif direction == "right" and j == A - 1:
          direction = "down"
      elif direction == "left" and j == 0:
          direction == "up"
      elif direction == "up" and i == 0:
          direction == "right"
      elif direction == "down" and i == A - 1:
          direction == "left"
          # print(count)
  # print(arr)
  return arr

# generateMatrix(3)