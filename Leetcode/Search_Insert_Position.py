class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Lower and upper bounds
        low, high = 0, len(nums)-1
        
        #Traverse search space
        while low<=high:
            
            #Get midpoint *use floor to get whole integer
            mid=(low+high)//2
            
            #If target already exists, return index
            if nums[mid]==target:
                return mid
            
            #If target is larger than mid indexed value, search right
            elif nums[mid]<target:
                low=mid+1
                
            #If target is smaller/equal to mid indexed value, search left
            else:
                high=mid-1
        
        return high+1
        #Runtime: 28ms