class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #1 - n
        left, right = 1, n
        
        #Binary Search
        while left <= right:
            
            #Get midpoint
            mid = int((left + right)/2)
            
            #If isBadVersion is False, search left side, else search the right side
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
        #Runtime: 16ms