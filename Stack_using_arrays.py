class Stack:
    def __init__(self, size):
        self.stack = [None] * size   
        self.top = -1

    def push(self, value):
        if self.top == len(self.stack) - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

    def isEmpty(self):
      return self.top == -1
      
    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack elements:", self.stack[:self.top+1])
      
stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("Top element:", stack.peek())
stack.pop()
stack.display()
print("Top element:", stack.peek())
print("Is stack empty?", stack.isEmpty())
