class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None: 
            self.front = self.rear = new_node
            print(f"Enqueued {data}")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued {data}")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty (Underflow)")
            return None
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:  
            self.rear = None
        print(f"Dequeued {dequeued_data}")
        return dequeued_data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        print("Queue elements:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
qu = Queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.display()
qu.dequeue()
print("Front element:", qu.peek())
qu.display()
