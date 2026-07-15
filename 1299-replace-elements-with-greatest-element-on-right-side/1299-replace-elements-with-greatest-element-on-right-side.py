class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        pref = -1

        for i in range(len(nums)-1,-1,-1):
            curr = nums[i]

            nums[i] =pref
            pref = max(pref,curr)
        return nums
           