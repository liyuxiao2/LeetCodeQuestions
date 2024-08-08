'''

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45


used memoization for this problem as well, beat 85% of other submissions
'''

class Solution(object):
    def __init__(self):
        self.cache = {}
        

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #if in cache return pre calculated value
        if(n in self.cache):
            return self.cache[n]
        
        
        #if its less than 4, n will be equivelant to the #of different orders to go up the steps
        if(n < 4):
            total_order = n
        else:
            total_order = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        self.cache[n] = total_order

        return total_order