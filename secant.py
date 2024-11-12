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
  x = random.uniform(-100, 100)
  y = random.uniform(-100, 100)
  arr = [(x, evaluate(f, to_replace, x)), (y, evaluate(f, to_replace, y))]
  while arr[-1][1] == arr[-2][1]:
    try:
      x = random.uniform(-100, 100)
      y = random.uniform(-100, 100)
      arr = [(x, evaluate(f, to_replace, x)), (y, evaluate(f, to_replace, y))]
    except:
      continue
  
  return arr

def solve(f, tolerance):
  to_replace = parse(f)
  arr = find_guesses(f, to_replace) 
  out = evaluate_recursively(arr, to_replace, f, tolerance) if arr[0][1] != 0 and arr[1][1] != 0 else 0
  for _ in range(1000):
    if out != "No root!":
      break
    else:
      try:
        arr = find_guesses(f, to_replace) 
        out = evaluate_recursively(arr, to_replace, f, tolerance) if arr[0][1] != 0 and arr[1][1] != 0 else 0
      except:
        continue
  
  return out

tolerance = 0.00000001
try:
  print(solve(input("Enter a function, use x as the variable: "), tolerance))
except:
  print("Check your function! It needs to be formatted in Python syntax.")