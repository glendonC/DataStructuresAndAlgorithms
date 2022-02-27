class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            #first one is supposed to be heavier
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            #but since we are doing negatives we have to check if second is greater than first
            if second>first:
                heapq.heappush(stones, first-second)
        stones.append(0)
        return abs(stones[0])