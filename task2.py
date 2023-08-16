class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        llist = []
        for i in nums:
            llist.append(i*i)
        llist.sort()
        return llist