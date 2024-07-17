#divide and conq algorithim
class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
            middle = self.partition(arr,low,high)
            
            
            #sorts the left
            self.quickSort(arr, low, middle-1)
            
            #sorts the right
            self.quickSort(arr, middle+1, high)
            
            
            
    def partition(self,arr,low,high):
        # code here
        
        #this is the pivot, we compare every element to the pivot
        pivot = arr[high]
        
        #this is the left most part of the index we are partitioning
        i = low
        
        
        
        for j in range(low, high):
            
            #if the left pointer
            if arr[j] <= pivot:
                
                arr[i], arr[j] = arr[j], arr[i]
                
                i += 1
        
        
        arr[i], arr[high] = arr[high], arr[i]
        
        
        #returns position where partition has ended
        return i