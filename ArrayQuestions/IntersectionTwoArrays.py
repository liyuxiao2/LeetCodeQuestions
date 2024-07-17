'''
Given two integer arrays nums1 and nums2, return an array of their 
intersection
Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000



Used 2 pointer approach. We sort the array first and then compare each element until we reach the end of one of the lists
time complexity O(NLogN+MLogM)
'''



class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #create pointers for nums1 and nums2
        nums_1_pointer, nums_2_pointer = 0, 0

        #where we store the intersecting values, maske it a set so we remove duplicates
        intersecting_vals = set()

        #sort both arrays
        nums1.sort()
        nums2.sort()



        while nums_1_pointer < len(nums1) and nums_2_pointer < len(nums2):
            #if equal, add value to intersection set
            if(nums1[nums_1_pointer] == nums2[nums_2_pointer]):
                intersecting_vals.add(nums1[nums_1_pointer])
                nums_1_pointer += 1
                nums_2_pointer += 1
            #else increment either pointer based on whether which one is greater
            elif(nums1[nums_1_pointer] > nums2[nums_2_pointer]):
                nums_2_pointer += 1
            else:
                nums_1_pointer += 1
        
        #revert set back to list
        intersceting_vals = list(intersecting_vals)


        return intersecting_vals
