# Description
'''Your task is to write function factorial.'''

# solution
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
  
  
# variation
def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n-1)
