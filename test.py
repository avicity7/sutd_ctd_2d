# Q1
total = 0

for i in range(4, 31):
  total += i

#Q2
for i in range(1, 23, 3):
  total += i

#Q3
for i in range(2, 15, 2):
  total += i**2

#Q4
def factorial(n):
  out = 1
  for i in range(2, n+1, 1):
    out *= i
  return i
    
#Q5
def get_total(n):
  out = 1
  for i in range(3, 2*n+2, 2):
    out *= i
  return out

