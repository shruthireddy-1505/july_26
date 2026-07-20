class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def fun(k):
            l = 0
            count = 0
            res = 0
            for r in range(0,len(nums)):
                if nums[r]%2!=0:
                    count +=1
                while count > k:
                    if nums[l]%2!=0:
                        count -=1
                    l +=1
                res += r-l+1
            return res

        return fun(k) - fun(k-1) 