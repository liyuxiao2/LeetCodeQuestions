"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
Greedy Algorithim: finds the most optimal solution locally in hopes of coming to a globally optimal solution
Time Comp: O(n)
Space Comp: O(1)
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # set buy price and max_profit
        buy_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            # if the buy price at i is lower, update buy variable
            if prices[i] < buy_price:
                buy_price = prices[i]

            # check if the profit now (sell - buy) is greater than current profit, update if it is
            if prices[i] - buy_price > max_profit:
                max_profit = prices[i] - buy_price

        return max_profit
