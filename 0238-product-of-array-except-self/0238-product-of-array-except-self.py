class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        pref = 1
        for i in range(0,n):
            ans[i] = pref
            pref *= nums[i]
        suff = 1
        for i in range(n-1,-1,-1):
            ans[i] = ans[i]*suff
            suff*= nums[i]
        return ans