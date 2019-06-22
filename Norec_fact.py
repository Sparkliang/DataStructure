# Data Structure-Ch5 Stack and Queue
# Recursive Function based Stack
# Liang
# 2019/4/18

from SStack import SStack

def norec_fact(n):
    res = 1
    st = SStack()
    while n > 0:
        st.push(n)
        n -= 1
    while not st.is_empty():
        res *= st.pop()
    return res