def your_course_username():
    """Return your course username. 

    >>> username = your_course_username()
    >>> username.startswith('cs61a-')
    True
    """
    return 'cs61a-linwen'

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    "*** YOUR CODE HERE ***"
    return max(a, b)*max(a, b) + max(min(a,b), c) * max(min(a,b), c)

def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.

    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, ...
    8
    """
    "*** YOUR CODE HERE ***"
    denominator = (n-1) * (n+1)
    while n > 0:
    	if denominator % n == 0:
    	    return n
    	else:
    		n = n-1

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result
def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return True

def t():
    "*** YOUR CODE HERE ***"
    return 1

def f():
    "*** YOUR CODE HERE ***"
    while 1:
    	print()

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    temp = int(n)
    length = 1
    print(temp)
    while temp != 1:
    	if temp % 2 == 0:
    		temp = temp / 2
    	else:
    		temp = temp * 3 + 1
    	print(temp)
    	length += 1

    return length

challenge_question_program = """
"*** YOUR CODE HERE ***"
"""