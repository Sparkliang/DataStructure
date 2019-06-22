# Data Structure-Ch4 String
# KMP_matching
# Liang
# 2019/4/9

# pnext
def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m-1:
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            # Optimized
            if p[i] == p[k]:
                #k = pnext[k]
                #pnext[i] = k
                pnext[i] = pnext [k]
            else:
                pnext[i] = k
            #pnext[i] = k
        else:
            k = pnext[k]
    return pnext

# Main function
def matching_KMP(t, p):
    pnext = gen_pnext(p)
    j, i = 0, 0
    n, m = len(t), len(p)
    while j<n and i<m:
        if i == -1 or t[j] == p[i]:
            j, i = j+1, i+1
        else:
            i = pnext[i]
    if i == m:
        return j-i
    return -1
