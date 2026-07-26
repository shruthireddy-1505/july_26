class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        d = {}
        for i in range(len(nums2)-1,-1,-1):
            while st and st[-1]<nums2[i]:
                st.pop()
            if not st:
                d[nums2[i]] = -1
            else:
                d[nums2[i]] = st[-1]
            st.append(nums2[i])
            
        res = []
        for i in nums1:
            res.append(d[i])
        return res

        