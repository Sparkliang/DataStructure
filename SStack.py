# Data Structure-Ch5 Stack and Queue
# Stack based sequence list
# Liang
# 2019/4/15

class StackUnderflow(ValueError):
    pass

# Stack based sequence list
class SStack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()

# Stack based link list

class LNode():
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_

class LStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("in SStack.top()")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem

# Bracket matching
def check_parens(text):
    """括号配对检查函数，text是被检查的正文串"""
    parens = "()[]{}"
    open_parens = "([{"
    opposite = {")":"(", "]":"[", "}":"{"}

    def parentheses(text):
        """括号生成器，每次调用返回text里的下一个括号及其位置"""
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
    st = SStack()
    for pr, i in parentheses(text):
        if pr is open_parens:
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print("Unmatching is found at", i, "for", pr)
            return False
        #else:
    print("All parentheses are correctly matched.")
    return True
