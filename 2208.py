class Solution:
    def halveArray(self, nums: List[int]) -> int:
        initialSum = sum(nums)
        halfSum = initialSum / 2
        movingSum = sum(nums)
        counter = 0

        def heapsort(iterable):
            h = []
            for value in iterable:
                heappush(h, value)
            return [heappop(h) for i in range(len(h))]

        nums=[-num for num in nums]
        nums = heapsort(nums)
        heapq.heapify(nums)
        while movingSum > halfSum:
            counter += 1
            movingSum += nums[0] / 2
            heapq.heapreplace(nums, nums[0] / 2)
        return counter
      
      """
      Runtime: 66.50%
      Memory: 11.86%
      """
