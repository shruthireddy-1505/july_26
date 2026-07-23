class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for i in s:
            if st and i == st[-1][0]:
                st[-1][1]+=1
                if st[-1][1] == k:
                    st.pop()
            else:
                st.append([i,1])
        ans  = ""
        for ch,cnt in st:
            ans+=ch*cnt
        return ans
        

        