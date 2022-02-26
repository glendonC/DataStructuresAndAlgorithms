class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # 
        
        minHeap = []
        
        #go through x, y in points
        for x, y in points:
            
            #get distance x^2+y^2  
            dist = (x**2)+(y**2)
            minHeap.append([dist,x,y])
        
        #reorders list to structure of a heap
        heapq.heapify(minHeap)
        res=[]
        
        #keep popping  from min heap
        while k>0:
            #we only want our x, y valyues
            dist, x,y=heapq.heappop(minHeap)
            
            res.append([x,y])
            k-=1
        return res