import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap=[]
        for point in points:
            dist=-(point[0]**2+point[1]**2)
            heapq.heappush(maxheap,[dist,point[0],point[1]])
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        res=[]
        while maxheap:
            dist,x,y=heapq.heappop(maxheap)
            res.append([x,y])
        return res
