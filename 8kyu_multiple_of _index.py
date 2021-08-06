# Description
'''
Return a new array consisting of elements which are multiple of their own index in input array (length > 1).'''

# variation 1
def multiple_of_index(arr):
    a = []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            a.append(arr[i])
    return a
  
  
  # variation 2
  return [arr[i] for i in range(1, len(arr)) if not arr % i]

# variation 3
return [n for i, n in enumerate(arr[1:], 1) if not n % i]
