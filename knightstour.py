#!/usr/bin/python3.6

# backtracking solution
def tracepath(i, j, n, step, matrix):
  # check if the step goes out of board
  if i > n-1:
    return False
  if i < 0:
    return False
  if j > n-1:
    return False
  if j < 0:
    return False
  # check if this step's house has already been visited
  if matrix[i][j] != 0:
    return False
  # make this step
  step += 1
  matrix[i][j] = step
  # if this is the last step them we find it
  if step == n*n:
    return True
  # Recursively check all possible movements
  if tracepath(i+2, j+1, n, step, matrix):
    return True
  elif tracepath(i+1, j+2, n, step, matrix):
    return True
  elif tracepath(i-1, j+2, n, step, matrix):
    return True
  elif tracepath(i-2, j+1, n, step, matrix):
    return True
  elif tracepath(i-2, j-1, n, step, matrix):
    return True
  elif tracepath(i-1, j-2, n, step, matrix):
    return True
  elif tracepath(i+1, j-2, n, step, matrix):
    return True
  elif tracepath(i+2, j-1, n, step, matrix):
    return True
  # If all possible moves fall into some negation then this step is not possible
  else:
    step = matrix[i][j] - 1 # Go back to the previous step
    matrix[i][j] = 0
    return False

def main(n):
  matrix = []
  for i in range(0, n):
    matrix.append([])
    for j in range(0, n):
      matrix[i].append(0)
  if tracepath(0, 0, n, 0, matrix):
    print ("This matrix below represents the board with each step being made by the horse:")
    for i in range(n-1, -1, -1):
      print (matrix[i])
  else:
    print ("No solution for board %sx%s" % (n,n))

if __name__ == "__main__":
  import sys
  main(int(sys.argv[1]))
