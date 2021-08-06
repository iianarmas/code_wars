# Description:
'''
The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return

[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) being the smallest one such as F(n) * F(n+1) > prod.'''


# long way (variation 1)
def productFib(prod):
    a, b = 0, 1

    new, lst, nums = [], [], []

    prod = str(prod)
    f = sum(map(int, prod)) * 2

    if f < 0:
        print('invalid')

    for i in range(f):
        a += b
        a, b = b, a
        lst.append(a)

    for k in range(len(lst) - 1):
        if k < int(prod):
            if int(prod) < lst[k] * lst[k + 1]:
                nums.append(lst[k])
                nums.append(lst[k + 1])
                new = [nums[i] for i in range(2)]
                new.append(False)
                return new

            elif int(prod) == lst[k] * lst[k + 1]:
                nums.append(lst[k])
                nums.append(lst[k + 1])
                new = [nums[i] for i in range(2)]
                new.append(True)
                return new
    if len(new) == 0:
        new.append(0)
        new.append(1)
        new.append(True)

    return new
  
  
  
 # variation 2

def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]


# variation 3
def productFib(prod):
    func = lambda a, b: func(b, a+b) if a*b < prod else [a, b, a*b == prod]
    return func(0, 1)
