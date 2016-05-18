
#!/usr/bin/env python

class Dll:
    def __init__(self):
        self.start = self.end = [None, 1, None]

    def append(self, val):
        old = self.end
        new = [old, val, None]
        old[2] = new
        self.end = new

    def prepend(self, val):
        new = [None, val, self.start]
        self.start[0] = new
        self.start = new

    def pop(self):
        val = self.end[1]
        self.end = self.end[0]
        return val

    def popleft(self):
        val = self.start[1]
        self.start = self.start[2]
        return val

def test():
    dll = Dll()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(10)
    # print ("dll.pop()", dll.pop())
    assert dll.pop() == 3
    assert dll.popleft() == 10
    assert dll.pop() == 2
    dll.append(6)
    assert dll.pop() == 6
    print ("tests passed..")
test()
