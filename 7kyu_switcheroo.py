# Description
'''Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb''''


# solution using replace()
def switcheroo(s):
    return ''.join(i.replace('a','-').replace('b', 'a').replace('-', 'b') for i in s)
  
# varitaion 2
def switcheroo(string):
    return ''.join( [ 'a' if s=='b' else 'b' if s=='a' else s for s in string ] )
  
# variation 3
def switcheroo(string):
    result = ''
    for letter in string:
        if letter == 'a':
            letter = 'b'
        elif letter == 'b':
            letter = 'a'
        result += letter
    return result
  
# variation 4
def switcheroo(string):
    return ((string.replace('a','x')).replace('b','a')).replace('x','b')
  
# variation 5
def switcheroo(s):
    return s.translate(str.maketrans('ab','ba'))
