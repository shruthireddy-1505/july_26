class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[]
        op,val=0,0
        for i in s:
            if i=="(":
                st.append(0)
            elif i==")":
                pop_ele=st.pop()
                if pop_ele==0:
                    val=1
                else:
                    val=pop_ele*2
                
                if not st:
                    op+=val
                else:
                    st[-1]+=val
        return op


                