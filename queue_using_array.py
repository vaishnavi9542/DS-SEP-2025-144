class Queue:
  def __init__(self,size):
    self.queue=[None]*size
    self.front=-1
    self.rear=-1
    self.size=size
  def isempty(self):
    return self.front==-1
  def isFull(self):
    return (self.rear+1)%self.size==self.front
  def enqueue(self,item):
    if self.isFull():
      print("Overflow of Queue")
      return 
    if self.isempty():
      self.front=self.rear=0
    else:
      self.rear=(self.rear+1)%self.size
    self.queue[self.rear]=item
    print(f"Enqueued {item}")
  def dequeue(self):
    if self.isempty():
      print("Underflow")
      return None
    value=self.queue[self.front]
    if self.front==self.rear:
      self.front=self.rear=-1
    else:
      self.front=(self.front+1)%self.size
    print(f"Dequeued {value}")
    return value
  def Front(self):
    if self.isempty():
      print("underflow")
      return None
    return self.queue[self.front]
  def display(self):
      if self.isempty():
        print("Queue is empty")
        return
      print("Queue elements:", end=" ")
      i = self.front
      while True:
        print(self.queue[i], end=" ")
        if i == self.rear:
            break
        i = (i + 1) % self.size
      print()

q=Queue(5)
q.enqueue(30)
q.enqueue(50)
q.enqueue(9)
q.display()
q.dequeue()
print("front element",q.Front())
q.display()
    
      
    
    
