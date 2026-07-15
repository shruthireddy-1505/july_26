class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tol = sum(nums)
        l = 0
        val = -1
        for i in range(len(nums)):
            r = tol - nums[i]
            if l == r:
                val = i
                break
            l += nums[i]
            tol = r
        return val
                