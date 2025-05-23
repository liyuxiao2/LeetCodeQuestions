"""

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).


I used memoization to complete this problem. We store the values already calculated in order to avoid repeated calculations.
Run time is much faster at the expense of memory.
"""


class Solution(object):
    # create a cache to store all of the vals
    def __init__(self):
        self.cache = {}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # return the value if it is already stored in the cache
        if n in self.cache:
            return self.cache[n]

        # calculate the value of fib(n)
        if n < 2:
            result = n
        else:
            result = self.fib(n - 1) + self.fib(n - 2)

        # store that value in the cache
        self.cache[n] = result

        return result
