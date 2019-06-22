# Data Structure-Ch5 Stack and Queue
# Backpack Problem based on stack
# Liang
# 2019/4/18

def knap_rec(weight, wlist, n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap_rec(weight - wlist[n-1], wlist, n-1):
        print("Item " + str(n)+ ":", wlist[n-1])
        return True
    if knap_rec(weight, wlist, n-1):
        return True
    else:
        return False
