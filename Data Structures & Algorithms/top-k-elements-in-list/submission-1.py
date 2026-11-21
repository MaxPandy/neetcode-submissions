import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        result=[]
        for num in nums:
            freq[num]=1+freq.get(num,0)

        heap=[(-value,key) for key,value in freq.items() ]
        heapq.heapify(heap)

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result