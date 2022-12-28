class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        def heapsort(iterable):
            h = []
            for value in iterable:
                heappush(h, value)
            return [heappop(h) for i in range(len(h))]

        piles = heapsort(piles)

        for i in range(k):
            smallest = piles[0]
            heapq.heapreplace(piles, smallest + (floor(-smallest / 2)))

        stones = 0
        for item in piles:
            stones += item
        return -stones
    
    """
    Runtime: 70.84%
    Memory: 9.61% :(
    """
