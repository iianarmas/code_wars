# Description
'''Implement a function named generateRange(min, max, step), which takes three arguments and generates a range of integers
from min to max, with the step. The first integer is the minimum value, the second is the maximum of the range and the third is the step. (min < max)'''

def generate_range(min, max, step):
    return [i for i in range(min, max+1, step)]
  
  
# variation 1
def generate_range(min, max, step):
  return list(range(min, max+1,step)
              
              
# variation 2
def generate_range(min, max, step):
  return [*range(min, max+1, step)]
