#!/usr/bin/python2.7

def tracepath(i, j, n, step, matrix):
  if i > n-1:
    return False
  if i < 0:
    return False
  if j > n-1:
    return False
  if j < 0:
    return False
  if matrix[i][j] != 0:
    return False
  step += 1
  matrix[i][j] = step
  if step == 64:
    return True
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
  elif tracepath(i+2, j-2, n, step, matrix):
    return True
  else:
    step = matrix[i][j] - 1
    matrix[i][j] = 0
    return False

def main(n):
  matrix = []
  for i in range(0, n):
    matrix.append([])
    for j in range(0, n):
      matrix[i].append(0)
  if tracepath(0, 0, n, 0, matrix):
    print "This matrix below represents the board with each step being made by the horse:"
    for i in range(n-1, -1, -1):
      print matrix[i]
  else:
    print "No solution for board %sx%s" % (n,n)

if __name__ == "__main__":
  import sys
  main(int(sys.argv[1]))
