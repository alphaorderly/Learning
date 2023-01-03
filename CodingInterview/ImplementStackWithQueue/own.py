class Queue:
    def __init__(self):
        self.stack = list()
    def enqueue(self, d):
        self.stack.append(d)
    def dequeue(self):
        deq = list(reversed(self.stack))
        ret = deq[len(deq)-1]
        deq = deq[:len(deq)-1]
        self.stack = list(reversed(deq))
        return ret
    def peek(self):
        return self.stack[0]
    def clear(self):
        self.stack.clear()

  
