class Solution:
    def printMinNumberForPattern(ob,S):
        ans = ""
        st = []
        no = 1
        for i in S:
            if i == "D":
                st.append(no)
                no += 1
            else:
                st.append(no)
                no += 1
                while st:
                    ans += str(st.pop())
        st.append(no)
        while st:
            ans += str(st.pop())
        return ans