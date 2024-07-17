#merge sort, div and conq
#modifies list in place
# time complexity O( n log n)
class Solution:
    
    #merge function acts as the "conquer"
    def merge(self,arr, l, m, r): 
        
        #initialize both sub arrays
        left_side_arr = arr[l: m+1]
        right_side_arr = arr[m+1: r+1]
        
        left_side_ptr, right_side_ptr, merge_arr_index = 0, 0, l
        
        #merge both arrays back into one array
        while left_side_ptr < len(left_side_arr) and right_side_ptr < len(right_side_arr):
            if(left_side_arr[left_side_ptr] <= right_side_arr[right_side_ptr]):
                arr[merge_arr_index] = left_side_arr[left_side_ptr]
                left_side_ptr += 1
            else:
                arr[merge_arr_index] = right_side_arr[right_side_ptr]
                right_side_ptr += 1
            merge_arr_index += 1
        
        
        #copy remaining elements into merge_arr
        while(left_side_ptr < len(left_side_arr)):
            arr[merge_arr_index] = left_side_arr[left_side_ptr]
            merge_arr_index += 1
            left_side_ptr += 1
        while(right_side_ptr < len(right_side_arr)):
            arr[merge_arr_index] = right_side_arr[right_side_ptr]
            merge_arr_index += 1
            right_side_ptr += 1
        
       
            
            
    def mergeSort(self,arr, l, r):
        if l > r:
            return
        else:
            
            mid = l + (r-l) // 2
            
            
            #divides the arr into smaller sub arr
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
    
            
            #conquers all of the sub arr and sorts them
            self.merge(arr, l, mid, r)
            
         

     
