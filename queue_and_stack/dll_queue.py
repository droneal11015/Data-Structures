import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    
    # Why is our DLL a good choice to store our elements?
    self.size = 0
    self.storage = DoublyLinkedList()

  def enqueue(self, value):
    self.size += 1
    self.storage.add_to_tail(value)
  
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      head_item = self.storage.head
      self.storage.remove_from_head()
      return head_item.value
    else:
      return None

  def len(self):
    return self.size
    
