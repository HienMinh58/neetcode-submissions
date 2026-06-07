class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t in '+-*/':
                b = int(st.pop())
                a = int(st.pop())
                if t == '+':
                    st.append(a+b)
                elif t == '-':
                    st.append(a-b)
                elif t == '*':
                    st.append(a*b)
                else:
                    st.append(a/b)
            else:
                st.append(t)
        return int(st[-1])
