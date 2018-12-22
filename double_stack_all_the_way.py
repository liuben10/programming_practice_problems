class Stack:

    def __init__(self):
        self.buf = []

    def ins(self, elem):
        self.buf.insert(0, elem)

    def pop(self):
        self.buf.pop(0)

    def peek(self):
        if (self.buf):
            return self.buf[0]
        else:
            return None

    def __str__(self):
        return str(self.buf)


class FindMaxDoubleStack:
    def __init__(self):
        self.main = Stack()
        self.max = Stack()

    def ins(self, elem):
        self.main.ins(elem)
        peeked = self.max.peek()
        if (peeked is None or elem > peeked):
            self.max.ins(elem)
        else:
            self.max.ins(peeked)

    def pop(self):
        self.max.pop()
        return self.main.pop()

    def max(self):
        return self.max.peek()

    def __str__(self):
        return "Main={}, Max={}".format(self.main, self.max)


if __name__ == '__main__':
    tds = FindMaxDoubleStack()
    tds.ins(3)
    tds.ins(4)
    tds.ins(2)
    tds.ins(5)
    tds.ins(4)
    print(tds)

