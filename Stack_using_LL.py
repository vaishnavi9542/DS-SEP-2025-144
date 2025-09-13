class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # top of stack

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  # new node points to the old top
        self.top = new_node       # update top
        print(f"Pushed: {data}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty (Underflow)")
            return None
        popped_data = self.top.data
        self.top = self.top.next  # move top to next
        print(f"Popped: {popped_data}")
        return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        print(f"Peek: {self.top.data}")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

st = Stack()
st.display()
st.push(10)
st.push(20)
st.push(30)
st.display()
st.pop()
st.peek()
st.display()
