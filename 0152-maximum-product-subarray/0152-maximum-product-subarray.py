class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref = 1
        suff = 1
        max_ans = float("-inf")
        for i in range(len(nums)):
            pref *= nums[i]
            suff *= nums[len(nums)-i-1]
            max_ans = max(max_ans,pref,suff)

            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1
        return max_ans

        