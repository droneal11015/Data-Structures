import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, item):
    if item < self.value:
      if not self.left:
        self.left = BinarySearchTree(item)
      else:
        self.left.insert(item)
    else:
      if not self.right:
        self.right = BinarySearchTree(item)
      else:
        self.right.insert(item)
    

  def contains(self, target):
    if self.value == target:
      return True
    else:
      if target < self.value:
        if not self.left:
          return False
        else:
          return self.left.contains(target)
      else:
        if not self.right:
          return False
        else:
          return self.right.contains(target)
        
     

  def get_max(self):
    if not self.right:
      return self.value
    return self.right.get_max()

  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb) 