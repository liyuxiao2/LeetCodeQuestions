"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""


# 1st approach
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        holder = {}
        for i in range(len(nums)):
            # check if val is in holder, and check if it meets the second condition
            if nums[i] in holder and abs(holder[nums[i]] - i) <= k:
                return True
            # otherwise, we update the the dictionary so that the value stores the latest index where it was seen
            holder[nums[i]] = i
        return False


# 2nd approcach
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        holder = {}
        for i, v in enumerate(nums):
            if v in holder and abs(i - holder[v]) <= k:
                return True
            holder[v] = i
        return False
