# In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

# variation 1
def well(x):
    count = 0
    for i in x:
        if i == 'good':
            count += 1
    if count == 1 or count == 2:
        return 'Publish!'
    elif count > 2:
        return 'I smell a series!'
    return 'Fail!'
  
# variation 2
def well(x):
  if 'good' in x:
    return 'I smell a series!' if x.count('good') > 2 else 'Publish!'
  else:
    return 'Fail!'

# variation 3
well = lambda x: ('Fail!','Publish!','I smell a series!')[('good' in x) + (x.count('good')>2)]
  
