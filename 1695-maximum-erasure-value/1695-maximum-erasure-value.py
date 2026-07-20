class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s =set()
        l = 0
        maxi = float("-inf")
        curr_sum = 0
        for r in range(len(nums)):
            while nums[r] in s:
                s.remove(nums[l])
                curr_sum -= nums[l]
                l +=1
            s.add(nums[r])
            curr_sum += nums[r]
            maxi = max(maxi,curr_sum)
        return maxi