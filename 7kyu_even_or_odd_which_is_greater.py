# Description

'''Given a string of digits confirm whether the sum of all the individual even digits are greater than the sum of all the indiviudal odd digits. Always a string of numbers will be given.

If the sum of even numbers is greater than the odd numbers return: "Even is greater than Odd"

If the sum of odd numbers is greater than the sum of even numbers return: "Odd is greater than Even"

If the total of both even and odd numbers are identical return: "Even and Odd are the same"'''



# solution
def even_or_odd(s):
    e, o = sum(int(i) for i in s if int(i) % 2 == 0), sum(int(i) for i in s if int(i) % 2 != 0)
    return "Even and Odd are the same" if e == o else ("Odd is greater than Even", "Even is greater than Odd")[e > o]
  
  
# variation 1
def even_or_odd(s):
    n=sum(x * (-1 if x % 2 else 1) for x in map(int,s))
    return 'Even is greater than Odd' if n > 0 else \
           'Odd is greater than Even' if n < 0 else \
           'Even and Odd are the same'

  
# variation 2
def even_or_odd(s):
    even = 0
    odd = 0
    for i in s:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    if even > odd:
        print(odd, even)
        return "Even is greater than Odd"
    elif even < odd:
        print(odd, even)
        return "Odd is greater than Even"
    print(odd, even)
    return "Even and Odd are the same"
