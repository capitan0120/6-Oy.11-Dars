class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxx=0
        nums.sort()

        for i in range(0, len(nums)-2):
            s1=nums[i]
            s2=nums[i+1]
            s3=nums[i+2]
            if s2+s3>s1 and s1+s3>s2 and s1+s2>s3:
                if maxx<(s1+s2+s3):
                    maxx=(s1+s2+s3)
        return maxx