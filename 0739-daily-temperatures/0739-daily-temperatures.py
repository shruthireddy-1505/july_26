class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        st = []
        for i in range(len(nums)-1,-1,-1):
            while st and st[-1][0] <= nums[i]:
                st.pop()
            if not st:
                res[i] = 0
            else:
                ans = st[-1][1] - i
                res[i] = ans
            st.append([nums[i],i])
        return res
        