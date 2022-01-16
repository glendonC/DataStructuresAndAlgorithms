class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        #Iterate over array
        for i in range(len(nums)):
            
            #If target is found, return its' index
            if nums[i]==target:
                return i
            
            #If target is smaller than the last value in array, the target would take the previous last index
            elif nums[i]>target:
                return i
        
        #Return length of array if the target is the greatest value
        return len(nums)
                
        #Runtime: 40ms