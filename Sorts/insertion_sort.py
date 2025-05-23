"""
Input: [23, 1, 4, 7, 8], n = 5
Output [1, 4, 7, 8, 23]


Time complexity : O(n^2)
space complexity O(1)
"""

# Sort the array using insertion sort


class Solution:
    def insert(self, alist, index):
        key = alist[index + 1]
        while index > 0 and alist[index] > key:
            alist[index + 1] = alist[index]
            index -= 1
        alist[index + 1] = key

    # Function to sort the list using insertion sort algorithm.
    def insertionSort(self, alist, n):
        for i in range(1, n):
            j = i - 1
            self.insert(alist, j, n)
        return alist
