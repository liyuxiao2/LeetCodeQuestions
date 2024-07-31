class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return 0


        prod_list = [1 for i in range(len(nums))]
        temp = 1

        for i in range(len(nums)):
            prod_list[i] = temp
            temp *= nums[i]
        
        temp = 1

        for i in range(len(nums)-1, -1, -1):
            prod_list[i] *= temp
            temp *= nums[i]
        

        return prod_list