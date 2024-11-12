from math import *
import random

def parse(f):
  return [i for i in range(len(f)) if f[i] == "x"]

def evaluate(f, to_replace, x):
  f = list(f)
  for i in to_replace:
    f[i] = f"({x})"
  y = eval("".join(f))

  return y

def evaluate_recursively(arr, to_replace, f, tolerance):
  x = arr[-1][0] - arr[-1][1] * (arr[-1][0] - arr[-2][0]) / (arr[-1][1] - arr[-2][1]) 
  y = evaluate(f, to_replace, x)
  arr.append((x, y))
  try:
    return evaluate_recursively(arr, to_replace, f, tolerance) if abs(arr[-1][1]) > tolerance else x
  except:
    return "No root!"

def find_guesses(f, to_replace):
  def find_two():
    x = random.uniform(-100, 100)
    y = random.uniform(-100, 100)
    return [(x, evaluate(f, to_replace, x)), (y, evaluate(f, to_replace, y))]

  arr = find_two()   

  while arr[-1][1] == arr[-2][1]:
    try:
      arr = find_two()
    except:
      continue
  
  return arr

def solve(f, tolerance):
  to_replace = parse(f)
  
  def get_solution():
    arr = find_guesses(f, to_replace) 
    return evaluate_recursively(arr, to_replace, f, tolerance) if arr[0][1] != 0 and arr[1][1] != 0 else 0
  
  out = get_solution()

  for _ in range(100000):
    if type(out) != str:
      break
    else:
      try:
        out = get_solution()
      except:
        continue
  
  return out

tolerance = 0.00000001
try:
  print(solve(input("Enter a function, use x as the variable: "), tolerance))
except:
  print("Check your function! It needs to be formatted in Python syntax.")