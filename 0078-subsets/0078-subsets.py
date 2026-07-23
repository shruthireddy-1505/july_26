class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range(2**n):
            sub = []
            for j in range(n):
                if (i>>j)&1:
                    sub.append(nums[j])
            res.append(sub)
        return res        