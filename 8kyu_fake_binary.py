# Description:
'''Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.'''


def fake_bin(x):
    return ''.join(map(lambda a: ('1', '0')[int(a) < 5], x))
  
  
# variation 2
def fake_bin(x):
  return ''.join(('1', '0')[i < '5'] for i in x)
