class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        st=[]
        for i,k in enumerate(temperatures):
            while st and k > st[-1][0]:
                stK, stI = st.pop()
                res[stK]=(i-stI)
            st.append([k,i])
        return res