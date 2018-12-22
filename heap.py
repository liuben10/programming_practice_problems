
def max_custom(a, b, custom_comparator):
    if (a is None and b is None):
        return None
    elif (a is None):
        return b
    elif (b is None):
        return a
    else:
        if (custom_comparator(a, b)):
            return a
        else:
            return b

def swap(buf, src, dest):
    tmp = buf[src]
    buf[src] = buf[dest]
    buf[dest] = tmp

def default_comparator(a, b):
    return a > b
    
class Heap:

    def __init__(self, comparator=default_comparator):
        self.buf = []
        self.comparator = comparator

    def set_comparator(self, comparator):
        self.comparator = comparator

    def push(self, value):
        self.buf.append(value)
        self.heapify()

    def pop(self):
        result = self.buf.pop(0)
        self.heapify()
        return result

    def pop_k(self, k):
        collected = []
        for i in range(k):
            collected.append(self.pop())
        return collected

    def heapify(self):
        self.heapify_help(0)

    def heapify_help(self, idx):
        lidx = 2 * idx + 1
        ridx = 2 * idx + 2
        leftc = None
        rightc = None
        if (lidx < len(self.buf)):
            self.heapify_help(lidx)
            leftc = self.buf[lidx]

        if (ridx < len(self.buf)):
            self.heapify_help(ridx)
            rightc = self.buf[ridx]

        maxc = max_custom(leftc, rightc, self.comparator)
        if (maxc is not None and self.comparator(maxc, self.buf[idx])):
            if (maxc == leftc):
                swap(self.buf, idx, lidx)
            else:
                swap(self.buf, idx, ridx)

        if (lidx < len(self.buf)):
            self.heapify_help(lidx)

        if (ridx < len(self.buf)):
            self.heapify_help(ridx)

    def __str__(self):
        return str(self.buf)


test_heap = Heap()
test_heap.push(5)
test_heap.push(3)
test_heap.push(10)
test_heap.push(2)
print(test_heap)
