""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a < b:
        a, b = b, a
    if a % b != 0:
        return gcd(b, a % b)
    else:
        return b


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        digit = n % 10
        if digit == 0:
            return ten_pairs(n // 10)
        else:
            return digit_cnt_in_n(10 - digit, n // 10) + ten_pairs(n // 10)

def digit_cnt_in_n(digit, n):
    cnt = 0
    while n > 0:
        if n % 10 == digit:
            cnt += 1
        n //= 10
    return cnt
