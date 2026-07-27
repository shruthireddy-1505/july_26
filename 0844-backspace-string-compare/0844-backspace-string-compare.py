class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def fun(temp):
            st = []
            for i in temp:
                if st and i=="#":
                    st.pop()
                else:
                    if i!="#":
                        st.append(i)
            return "".join(st)

        return fun(s) == fun(t)

        


        