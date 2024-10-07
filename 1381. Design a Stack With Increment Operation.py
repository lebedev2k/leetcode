from collections import deque
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.length = 0
        self.stack = []
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.length += 1
        

    def pop(self) -> int:
        if self.length == 0: return -1
        self.length -= 1
        return self.stack.pop(self.length)
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val