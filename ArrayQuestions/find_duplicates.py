'''

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3

'''

class Solution(object):
    
    
    #first sol. I came up with  (non-optimal approach), also did not O(1) space comp
    #Used a hashmap stored every value, if a value is seen again return that value
    def findDuplicate(self, nums):
        #store in dict
        ans_key = {}

        for i in range(len(nums)):
            if(nums[i] in ans_key):
                return nums[i]
            else:
                ans_key[nums[i]] = 1
        return 0
    
    
    def optimalFindDuplicates(self, nums):
        return None
    
    