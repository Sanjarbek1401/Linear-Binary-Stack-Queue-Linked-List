# Linear Search
def linear_search(arr, x):
 
  for i in range(len(arr)):
    if arr[i] == x:
      return i
  return -1

# Example usage
arr = [2, 4, 6, 8, 10]
x = 8
index = linear_search(arr, x)
if index != -1:
  print(f"Element {x} found at index {index}")
else:
  print(f"Element {x} not found")


# Binary Search
def binary_search(arr, x):

  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == x:
      return mid
    elif arr[mid] < x:
      low = mid + 1
    else:
      high = mid - 1
  return -1

# Example usage
arr = [2, 4, 6, 8, 10]
x = 8
index = binary_search(arr, x)
if index != -1:
  print(f"Element {x} found at index {index}")
else:
  print(f"Element {x} not found")

# Stack
class Stack:
  
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.is_empty():
      return self.items.pop()
    else:
      return None

  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    else:
      return None

  def is_empty(self):
    return len(self.items) == 0

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(f"Popped item: {stack.pop()}")
print(f"Top item: {stack.peek()}")

# Queue
class Queue:

  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    if not self.is_empty():
      return self.items.pop(0)
    else:
      return None

  def peek(self):
    if not self.is_empty():
      return self.items[0]
    else:
      return None

  def is_empty(self):
    return len(self.items) == 0

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(f"Dequeued item: {queue.dequeue()}")
print(f"Front item: {queue.peek()}")

# Linked List
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def print_list(self):
    current_node = self.head
    while current_node:
      print(current_node.data, end=" ")
      current_node = current_node.next
    print()

# Example usage
linked_list = LinkedList()
linked_list.insert_at_beginning(5)
linked_list.insert_at_end(10)
linked_list.insert_at_beginning(15)
linked_list.print_list()  # Output: 15 5 10 