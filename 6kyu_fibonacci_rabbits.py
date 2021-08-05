# Description
'''In his publication Liber Abaci Leonardo Bonacci, aka Fibonacci, posed a problem involving a population of idealized rabbits. These rabbits bred at a fixed rate, matured over the course of one month, had unlimited resources, and were immortal.

Beginning with one immature pair of these idealized rabbits that produce b pairs of offspring at the end of each month. Create a function that determines the number of pair of mature rabbits after n months.

To illustrate the problem, consider the following example:

fib_rabbits(5, 3) returns 19'''

# variation 1
def fib_rabbits(n, b):
    adult, total = 1, 1
    
    for i in range(n-1):
        total, adult = adult, adult + (total * b)
    return 0 if total - n == 1 else (total, 1)[total - n == 0]
  
  
  # variation 2
def fib_rabbits(n, b):
    adult, total = 1, 0

    for i in range(n):
        total, adult = total + adult, total * b
    return total
