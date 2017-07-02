class StackWithMin:
  def __init__(self):
    self.arr = []
    self.end = 0
    self.min = []

  def push(self, val):
    self.arr.extend([None] * (self.end + 1 - len(self.arr)))
    self.min.extend([None] * (self.end + 1 - len(self.min)))
    self.arr[self.end] = val
    if self.end == 0:
      self.min[self.end] = val
    else:
      self.min[self.end] = min(val, self.arr[self.end - 1])
    self.end += 1

  def pop(self):
    if self.end == 0:
      raise IndexError("Stack is empty")
    end = self.arr[self.end - 1]
    self.arr[self.end - 1] = None
    self.end -= 1
    return end

  def getMin(self):
    if self.end > 0:
      self.end -= 1
      return self.min[self.end]
    else:
      raise IndexError("Stack is empty")
