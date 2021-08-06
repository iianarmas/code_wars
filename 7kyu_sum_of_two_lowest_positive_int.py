'''Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.'''

# variation 1
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return sum(numbers[:2])
  
  
# variation 2
def sum_two_smallest_numbers(numbers):
  return sum(sorted(numbers)[:2])
