class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Iterate over array, using range/len to access specific index
        for i in range(len(nums)):
            #Check if indexed value matches target. Returns index if true
            if(nums[i]==target):
                return i
        #Default return value if target isn't found
        return -1
        
        #Without comments, runtime is 192ms