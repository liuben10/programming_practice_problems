class lnode:
    def __init__(self, val):
        self.val = val
        self.next = None

def rot_list(listy, k):
    fp = listy
    tp = listy
    ylen = len_l(listy)
    kmod = ylen - (k % ylen)
    prev = None
    for i in range(kmod):
        prev = fp
        fp = fp.next

    if fp == tp:
        return listy

    prev.next = None

    end = fp
    while(end.next is not None):
        end = end.next

    end.next = tp

    return fp
        
            
def len_l(listy):
    res = 0
    while(listy is not None):
        res += 1
        listy = listy.next
    return res

def printlist(listy):
    resstr = ""
    while(listy is not None):
        resstr += str(listy.val) + "->"
        listy = listy.next
    print(resstr)

e = lnode(5)
f = lnode(6)
g = lnode(7)
h = lnode(8)
d = lnode(4)
c = lnode(3)
b = lnode(2)
a = lnode(1)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h

printlist(a)

printlist(rot_list(a, 5))
