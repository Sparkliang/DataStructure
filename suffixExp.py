# Data Structure-Ch5 Stack and Queue
# Suffix expression based SStack
# Liang
# 2019/4/16
from SStack import SStack

def suffix_exp_evaluator(line):
    return suf_exp_evluator(line.split())

class ESStack(SStack):
    def depth(self):
        return len(self._elems)

def suf_exp_evluator(exp):
    operators = "+-*/"
    st = ESStack()            # Stack with depth function

    for x in exp:
        if x not in operators:
            #print('1', x)
            #print(type(x))
            f = float(x)
            st.push(f)
            continue

        if st.depth() < 2:
            raise SyntaxError("Short of operand(s).")
        a = st.pop() # second object
        b = st.pop() # first object

        if x == "+":
            c = a+b
        elif x == "-":
            c = b-a
        elif x == "*":
            c = b*a
        elif x == "/":
            c = b/a
        else:
            break

        st.push(c)

    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s).")

def suffix_exp_calculator():
    while True:
        try:
            line = input("Suffix Expression: ")
            if line == "end":
                return None
            print(line)
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print("Error:", type(ex), ex.args)

if __name__ == "__main__":
    suffix_exp_calculator()

