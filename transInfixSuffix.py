# Data Structure-Ch5 Stack and Queue
# transform infix to suffix
# Liang
# 2019/4/16

from SStack import SStack
import suffixExp as se

priority = {"(":1, "+":3, "-":3, "*":5, "/":5}
infix_opreators = "+-*/()"

def trans_infix_suffix(line):
    st = SStack()
    exp = []

    for x in tokens(line):
        if x not in infix_opreators:
            exp.append(x)
        elif st.is_empty() or x == "(":
            st.push(x)
        elif x == ")":
            while not st.is_empty() and st.top() != "(":
                exp.append(st.pop())
            if st.is_empty():
                raise SyntaxError("Missing '('.")
            st.pop()
        else:
            while (not st.is_empty() and priority[st.top()] >= priority[x]):
                exp.append(st.pop())
            st.push(x)

    while not st.is_empty():
        if st.top() == "(":
            raise SyntaxError("Extra '('.")
        exp.append(st.pop())

    return exp

def tokens(line):
    i, llen = 0, len(line)
    while i < llen: # Operator
        while line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_opreators:
            yield line[i]
            i += 1
            continue

        j = i+1
        while (j<llen and not line[j].isspace() and
                line[j] not in infix_opreators):
            if ((line[j] == 'e' or line[j] == 'E')
                and j+1 <llen and line[j+1] == '-'):
                j += 1
            j += 1
        yield line[i:j]
        i = j

def test_trans_infix_suffix(s):
    print(s)
    print(tokens(s))
    print(trans_infix_suffix(s))
    print("Value:", se.suf_exp_evaluator(trans_infix_suffix(s)))