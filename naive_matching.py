# Data Structure-Ch4 String
# naive_matching
# Liang
# 2019/4/8

def naive_matching(t, p):
    m, n = len(p), len(t)
    i, j = 0, 0
    while i<m and j<n:
        if p[i] == t[j]:
            i, j = i + 1, j + 1
        else:
            i, j = 0, j - 1 + 1
    if i == m:
        return j - i
    return -1