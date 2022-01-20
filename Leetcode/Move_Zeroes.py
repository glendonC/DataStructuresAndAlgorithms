class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arrLength = len(nums)
        i = 0
        
        while i < arrLength:
            #Add zero to back of list, decreasing the count for the loop backwards
            if nums[i] == 0:
                nums.append(nums.pop(i))
                arrLength -= 1
            #Increment iteration for loop
            else:
                i += 1
        #Runtime: 144ms