class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        st = []
        n = len(nums)
        for i in range(((n*2)-1),-1,-1):
            while st and st[-1]<=nums[i%n]:
                st.pop()
            if not st:
                res[i%n] = -1
            else:
                res[i%n] = st[-1]
            st.append(nums[i%n])
        return res